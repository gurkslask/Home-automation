#import bokeh as bk
#import pandas as pd
import sqlite3 as lite
import datetime as dt
import time


def LoadFromSQL():
    cur_time = time.time()
    conn = lite.connect('/home/pi/Projects/Home-automation/data.db')
    cur = conn.cursor()
    with conn:
        print('select * from VS1_GT3 where Time between {0:.0f} and {0:.0f}'.format(
            cur_time,
            #3 days
            cur_time - 3 * 3600
            ))

        cur.execute("""
            select *
            from VS1_GT3
            where Time between '{0:.0f}' and '{0:.0f}'
            """
                    .format(
                        cur_time,
                        cur_time - 3 * 3600
                        ))

        data = cur.fetchall()
    print(len(data))
    #pd_data = pd.DataFrame(data, columns=['Time, Temp'])
    #print(pd_data)
    return data


def PlotBokeh():
    pass

if __name__ == '__main__':
    LoadFromSQL()
