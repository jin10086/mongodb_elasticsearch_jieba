# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
import random
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'d_c0="AFCA5yV5egqPTnSeQbDOQsMpajNMESwoe6w=|1472797731"; _za=66d17f0f-458a-4fd3-b858-1c7aadef3ace; _zap=d8a0a687-644f-40c5-ad28-0f967ae3bf48; _xsrf=fca7c65ace1a2b493e0c2ae55531dea6; __utmt=1; BCSI-CS-d98f28e836c7ac17=2; q_c1=3a125e46c8874a7495ede42f639aaf8a|1474353661000|1474353661000; l_cap_id="ZTk3MjYzNGY2YzY4NDZkZWE2MjJjZGU5YmRkYzQzNTQ=|1474353661|8bac187a55006eda2031e1b2c21e5ebc3b39fe1d"; cap_id="YjQzOWYxMGZmOGQ4NDc4MzkyZjQwOWIyNzMwNGI5YWM=|1474353661|ccec2d2da985f1dae3c928237ddd05ee43e4b189"; __utma=51854390.1865594643.1474337211.1474337211.1474353350.2; __utmb=51854390.23.9.1474353644312; __utmc=51854390; __utmz=51854390.1474261792.5.4.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|2=registration_date=20160213=1^3=entry_date=20160920=1; login="ZmE4Y2M0MDIwMmYzNDA4NWE0NmMyMTZlNzE4ZjA0YzI=|1474353867|5ea81450c50275d4db5fd6b879653c7ac3fb260d"; a_t="2.0AGCANeLtjAoXAAAAy2cIWABggDXi7YwKAFCA5yV5egoXAAAAYQJVTctnCFgAT1XQCs2xxHuyQq5xmqb8b9m_P9JGP499JRGm4ULQnGyXAxirmNiABw=="; z_c0=Mi4wQUdDQU5lTHRqQW9BVUlEbkpYbDZDaGNBQUFCaEFsVk55MmNJV0FCUFZkQUt6YkhFZTdKQ3JuR2Fwdnh2MmI4XzBn|1474353867|f42870c245bd0d9267a2fe3b2e6427a8a21e2272; n_c=1',
'Host':'www.zhihu.com',
'Pragma':'no-cache',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}  
def getimg(i):
    textarea = etree.HTML(i).xpath('//div[@class="feed-content"]/div/div[@class="zm-item-rich-text expandable js-collapse-body"]/textarea/text()')[0]
    
    srclist = etree.HTML(textarea).xpath('//img/@src')
    if len(srclist) > 1:
        return random.sample(srclist,2)
    else:
        return srclist
        
if __name__ == '__main__':
    url = 'https://www.zhihu.com/node/TopicFeedList'
    topurl = 'https://www.zhihu.com/topic'
    x = requests.get(topurl,headers=headers,proxies=proxies,verify=False)
    _xsrf = etree.HTML(x.content).xpath('//input[@name="_xsrf"]/@value')[0]
    headers['X-Xsrftoken'] = _xsrf
    data = {'method':'next',
            'params':'{"offset":0,"topic_id":388,"feed_type":"timeline_feed"}'}
    z = requests.post(url,headers=headers,proxies=proxies,verify=False,data=data)
    all = json.loads(z.content)['msg']
    for i in all:
        title = etree.HTML(i).xpath('//div[@class="feed-content"]/h2/a/text()')
        href = etree.HTML(i).xpath('//div/link/@href')
        data_score = etree.HTML(i).xpath('//div/@data-score')
        absxxx = etree.HTML(i).xpath('//div[@class="feed-content"]/div/div[@class="zm-item-rich-text expandable js-collapse-body"]/div/text()')
        img = etree.HTML(i).xpath('//img/@src')
        if img != '':
            retimg = getimg(i)
            print retimg
        

