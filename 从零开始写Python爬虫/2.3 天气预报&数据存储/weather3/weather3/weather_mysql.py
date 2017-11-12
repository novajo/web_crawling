# -*- coding:utf-8 -*-
import pymysql


def insert(date, week, temperature, weather, wind, img):
    try:
        conn = pymysql.connect(host='@@@',
                               user='@@@', passwd='@@@',
                               db='scrapyDB',
                               port=3306,
                               charset='utf8')
        cur = conn.cursor()
        ins = 'insert into weather (date, week, temperature, weather, wind, img) values ("%s", "%s", "%s", "%s", "%s", "%s");' % (date, week, temperature, weather, wind, img)
        status = cur.execute(ins)
        if status == 1:
            print('Done')
        else:
            print('Failed')
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(repr(e))
