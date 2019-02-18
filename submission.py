
from worldquant.api import WQClient
from worldquant.api.submission import WQSubmissionClient
from worldquant.exceptions import WQException
import random
import os
import time

user ='***'
pswd = '***'

client = WQClient()
client.login(user, pswd)
print(5)
f = open('AlphaIds2.txt')
submit = WQSubmissionClient(client)
overview = client.myalphas.alphasoverview()
for id in f:
    try:
        if id:
            id = id.strip()
            info = client.myalphas.alphainfo(id)
            settings = info['AlphaSettings']
            sim_sum = info['AlphaSimSum']
            average_sum = sim_sum[-1]
            if average_sum['Sharpe'] > 1.25:
                if average_sum['ShortCount'] + average_sum['LongCount'] > 10 :
                    #print('Good')
                    result = submit.start(id)
                    print(f"{id} : {result}")
                    time.sleep(10)
#              else:
                #print("notGood")
    except KeyError :
        print("Err with:", id)
        time.sleep(10)
