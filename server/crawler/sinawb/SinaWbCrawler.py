"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   17/8/7
Desc:   sina weibo crawler
"""

BASE_URL = 'https://api.weibo.com/2/'
NEW_PUSH_URL = BASE_URL + 'statuses/user_timeline.json'
class SinaWbCrawler() :
    def __init__(self):
        print 'sina weibo crawler.'

    def do(self):
        return '--- sina wei bo msg.'

    def getAccessToken(self):
        return "1234"

if __name__ == '__main__':
    sinaWbCrawler = SinaWbCrawler()
    print sinaWbCrawler.do()