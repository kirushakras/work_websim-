import json
from collections import namedtuple

import requests

from .exceptions import WQJobProgressError, WQAuthenticationError



AlphasOverview = namedtuple('AlphasOverview', ['NumFailedAlphas', 'NumOSAlphas', 'NumProdAlphas', 'NumTotalAlphas'])
AlphaData = namedtuple('AlphaData', ["AlphaClientId", "Code", "IsInOS", "Hidden", "IsTeamAlpha", "Favorite", "AlphaName", "CodeType", "DateCreated", "Color", "Region", "Universe", "Sharpe", "Returns", "TurnOver", "Margin"])
AlphaData.__new__.__defaults__ = (None,) * len(AlphaData._fields)


class WQClient(object):
    def __init__(self):
        self.jar = None
        self.email = None
        self.password = None

    def do_query(self, *args, **kwargs):
        if self.jar is not None:
            if 'cookies' not in kwargs: kwargs['cookies'] = self.jar
            #self.jar['_xsrf'] = XSRF_TOKEN
            #print(kwargs['cookies'])

        kwargs['allow_redirects'] = False
        r = requests.request(*args, **kwargs)

        location = r.headers.get('Location', None)
        is_login_required = location is not None and location.startswith('/login')
        if is_login_required:
            self.login(self.email, self.password)
            return self.do_query(*args, **kwargs)
        #self.jar = r.cookies
        #print('OUT COOKIES', self.jar)
        #print('OK', r.text)
        return r

    def do_post(self, *args, **kwargs):
        return self.do_query('POST', *args, **kwargs)

    def do_get(self, *args, **kwargs):
        return self.do_query('GET', *args, **kwargs)

    def login(self, email, password):
        r = self.do_post('https://websim.worldquantchallenge.com/login/process', data={
            'EmailAddress': email,
            'Password': password,
            'next': '',
            'g-recaptcha-response': '',
        })

        result = r.json()
        if result['error'] is not None:
            raise WQAuthenticationError(result['error'])

        self.jar = r.cookies
        self.email = email
        self.password = password

    def get_alphasoverview(self):
        r = self.do_get('https://websim.worldquantchallenge.com/myalphas/alphasoverview')
        return AlphasOverview(**r.json()[0])

    def get_alphadata(self, page=1, limit=40, region=None, universe=None):
        clauses = []
        if region is not None:
            clauses.append({"Region":["{,}",region]})
        if universe is not None:
            clauses.append({"Universe":["{,}",universe]})

        fields = ["LongCount", "Returns","Color","Universe","CodeType","AlphaName","Hidden","Code","Margin","TurnOver","IsInOS","Region","IsTeamAlpha","DateCreated","Sharpe","Favorite"]
        limit = {"limit":limit,"pageNumber":page}
        sort = {"colName":"DateCreated","sortOrder":"DESC"}

        r = self.do_post('https://websim.worldquantchallenge.com/myalphas/alphadata', data={
            'type': 'is',
            #'_xsrf': XSRF_TOKEN,
            'fields': json.dumps(fields),
            'clauses': json.dumps(clauses),
            'limit': json.dumps(limit),
            'sort': json.dumps(sort),
        }, headers={
            'Content-Type': 'application/x-www-form-urlencoded',
        })

        result = r.json()
        return (AlphaData(**entry) for entry in result['data'])

    def get_alphainfo(self, alpha_id):
        r = self.do_post('https://websim.worldquantchallenge.com/alphainfo', data={
            "args": json.dumps({
                "alpha_list": [alpha_id],
            })
        })

        result = r.json()
        return result['result']['alphaInfo']

    def simulate(self, code, region, universe,decay = 21):
        args = [{
            "delay": "1",
            "unitcheck": "off",
            "univid": universe,
            "opcodetype": "EXPRESSION",
            "opassetclass": "EQUITY",
            "optrunc": 0.1,
            "code": code,
            "region": region,
            "opneut": "none",
            "IntradayType": None,
            "tags": "equity",
            "decay": decay,
            "dataviz": "0",
            "backdays": 512,
            "simtime": "Y5"
        }]

        print(args)
        r = self.do_post('https://websim.worldquantchallenge.com/simulate', data={
            'args': json.dumps(args),
        })
        print(r.text)
        r = r.json()
        print(r)
        return r['result'][0]

    def get_jobdetails(self, jobid):
        r = self.do_post('https://websim.worldquantchallenge.com/job/details/' + str(jobid))
        return r.json()

    def get_jobprogress(self, jobid):
        r = self.do_post('https://websim.worldquantchallenge.com/job/progress/' + str(jobid))
        progress = r.json()
        if progress == 'DONE':
            return 100
        if progress == 'ERROR':
            raise WQJobProgressError('Job ' + str(jobid) + ' has been stopped with error')
        return int(progress)

    def get_joberror(self, jobid):
        r = self.do_post('https://websim.worldquantchallenge.com/job/error/' + str(jobid))
        return r.json()
