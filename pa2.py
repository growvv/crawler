from requests_html import HTMLSession
import time
import datetime
import pytz

def get_content():
    session = HTMLSession()
    url = 'https://www.cnblogs.com/lfri/p/9362441.html'
    r = session.get(url)
    # print(r.html.text)
    r.html.render(scrolldown=1)  #下拉3次
    followers = r.html.find('#profile_block > a:nth-child(5)', first=True).text
    followees = r.html.find('#profile_block > a:nth-child(7)', first=True).text
    # print(followers, followees)

    score = r.html.find('#sidebar_scorerank > div > ul > li.liScore', first=True).text
    rank = r.html.find('#sidebar_scorerank > div > ul > li.liRank', first=True).text
    score = int(score.split()[2])
    rank = int(rank.split()[2])
    # print(score, rank)

    tz = pytz.timezone('Asia/Shanghai') #东八区
    t = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    # print(t)

    with open('record.md', 'a', encoding="utf-8") as f:  #使用utf-8编码
        s = f'{t} 粉丝{followers} 关注{followees} 积分{score} 排名{rank}<br>'
        print(s)
        f.write(s + '\n')


if __name__ == '__main__':
    get_content()
