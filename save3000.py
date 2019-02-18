import sqlite3
from worldquant.api import WQClient
from worldquant.exceptions import WQException

email = '***'
password = '***'
f = open('1.txt', 'w')

def save(region, universe):
    client = WQClient()
    client.login(email, password)

    connection = sqlite3.connect(region + ".db")
    cursor = connection.cursor()
    sql_command = " CREATE TABLE IF NOT EXISTS {universe} (id INTEGER PRIMARY KEY, alpha_code TEXT, long_count INTEGER, short_count INTEGER, pnl INTEGER, sharpe INTEGER, fitness INTEGER, return INTEGER, drawdown INTEGER, turnover INTEGER, margin INTEGER, used INTEGER, delay INTEGER, sub INTEGER, super INTEGER, error INTEGER, DateCreated TEXT);".format(universe=universe)
    cursor.execute(sql_command)
    
    overview = client.myalphas.alphasoverview()
    print(overview)
    
    page_size = 100
    for i in range(0, overview.NumTotalAlphas, page_size):
        for alpha in client.myalphas.alphadata(page=i/page_size, limit=page_size, region=region, universe=universe):
            print('Alpha id', alpha.AlphaClientId)
            a = alpha.AlphaClientId
            info = client.myalphas.alphainfo(alpha.AlphaClientId)
            settings = info['AlphaSettings']
            sim_sum = info['AlphaSimSum']
            average_sum = sim_sum[-1]
            print(average_sum)
            
            if average_sum['Sharpe'] > 0.8 or average_sum['Sharpe']< - 0.8:
                if average_sum['ShortCount'] + average_sum['LongCount'] > 40 :
                    print('Good'+str(info))
                    f.write(a +'\n')
                    
                    format_str = """INSERT INTO TOP200(id, alpha_code, long_count, short_count, pnl, sharpe, fitness, return, drawdown, turnover, margin, used, delay, sub, super, error, DateCreated) VALUES (NULL, "{Code}", "{LongCount}", "{ShortCount}", "{PnL}", "{Sharpe}", "{Fitness}", "{Returns}", "{DrawDown}", "{TurnOver}", "{Margin}", "0", "{Delay}", "0", "0", "0","{DateCreated}");"""
                    sql_command = format_str.format(**dict(average_sum, **settings))
                    cursor.execute(sql_command)
                    connection.commit()
                    

save('USA', 'TOP200')
