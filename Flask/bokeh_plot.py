import bokeh as bk
import pandas as pd
import sqlite3 as lite
import datetime as dt

def LoadFromSQL():
    conn = lite.connect('~/Projects/Home-automation/data.db')
    cur = conn.cursor()
    with conn:
        cur.execute('select * from VS1_GT3  between {} and {}'.format(
            dt.datetime.now(), dt.timedelta(hours=-3)))
        data = cur.fetchall()
    pd_data = pd.DataFrame(date, columns=['Time, Temp'])
    print(pd_data)


def PlotBokeh():
    pass