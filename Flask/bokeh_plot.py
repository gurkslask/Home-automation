#import bokeh as bk
#import pandas as pd
import sqlite3 as lite
import datetime as dt


def LoadFromSQL():
    conn = lite.connect('/home/pi/Projects/Home-automation/data.db')
    cur = conn.cursor()
    with conn:
        print('select * from VS1_GT3 where Time between {} and {}'.format(
            dt.datetime.now(),
            (dt.datetime.now() - dt.timedelta(days=3))
            ))

        cur.execute("""
            select *
            from VS1_GT3
            where Time between "{}" and "{}"
            """
                    .format(
                        dt.datetime.now(),
                        dt.datetime.now() - dt.timedelta(days=10)
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
