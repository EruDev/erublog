import requests
import sqlite3
import pymysql

# 建立连接
# conn = pymysql.connect(user='root', password='root', host='127.0.0.1', db='douban', charset='utf8')
conn = sqlite3.connect('app.db')
try:
    cur = conn.cursor()
    print('ok')
    # cur.execute('DROP TABLE IF EXISTS douban')
    # create_table = '''CREATE TABLE douban (id INT PRIMARY KEY,title VARCHAR(50),directors VARCHAR(50), rate VARCHAR(20), pic VARCHAR(255), url VARCHAR(255))'''
    # cur.execute(create_table)

    start = 0
    while start <= 100:
        url = 'https://movie.douban.com/j/new_search_subjects?sort=T&tags=%E6%82%AC%E7%96%91&start={}'.format(str(start))

        response = requests.get(url).json()['data']
        # print(response)
        for item in response:
            # print(item))
            title = item['title']
            directors = ','.join(item['directors'])
            rate = item['rate']
            pic = item['cover']
            url = item['url']
            # sql = 'INSERT INTO douban (title, directors, rate, pic, url) VALUES (%(title)s, %(directors)s, %(rate)s, %(pic)s, %(url)s)'
            # values = {
            #     'title': title,
            #     'directors': directors,
            #     'rate': rate,
            #     'pic': pic,
            #     'url': url,
            # }
            cur.execute('INSERT INTO dou_ban (id, title, directors, rate, pic, url) VALUES (null, "{title}","{directors}", "{rate}","{pic}","{url}")'.format(title=title, directors=directors, rate=rate, pic=pic, url=url))
            conn.commit()
            print('成功插入一条数据~')
            print('电影名: {} 导演: {} 评分: {} 封面图: {} url: {} '.format(title, directors, rate, pic, url))

        start += 20
except Exception as e:
    conn.rollback()
    print(e)