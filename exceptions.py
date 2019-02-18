class WQException(Exception):
    pass

class WQJobProgressError(WQException):
    jobid = None
    def __init__(self, jobid):
        self.jobid = jobid

class WQAuthenticationError(WQException):
    pass


