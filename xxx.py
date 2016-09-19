# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json
 

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'q_c1=7685ad16cbec4953aeb03f3480df24a6|1472797718000|1472797718000; d_c0="AFCA5yV5egqPTnSeQbDOQsMpajNMESwoe6w=|1472797731"; _za=66d17f0f-458a-4fd3-b858-1c7aadef3ace; _zap=d8a0a687-644f-40c5-ad28-0f967ae3bf48; _xsrf=fca7c65ace1a2b493e0c2ae55531dea6; __utmt=1; l_cap_id="NTI3NDQ1NTE1YzRjNGZiZDg0NTlkYTE2ZDc5YWY2MjM=|1474263170|875706582b0f7a088042b2f869e9e9f26f6b6287"; cap_id="YmFlZGYxZjM0NmFlNDQ2NTkzYzJiY2UwN2E4YjQzNzM=|1474263170|811c1e4f8692cfbc40671d4fa6faaf7551850b11"; login="MzMxOWYzNjkyODczNDJiM2ExZDUxMTEwNTM5ZDA5NmE=|1474263178|8859cb14e40ca37dab62237bac7ae40d43acf34c"; n_c=1; __utma=51854390.1743166441.1474033864.1474256821.1474261792.5; __utmb=51854390.19.9.1474262542557; __utmc=51854390; __utmz=51854390.1474261792.5.4.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20160916=1^3=entry_date=20160902=1; a_t="2.0AGCANeLtjAoXAAAA3AUHWABggDXi7YwKAFCA5yV5egoXAAAAYQJVTYoFB1gAWYoCmLIl6ISemzDcI0h7NklIF9sqp4kpvQ7IlNv2Mz-d7xy96MnzkA=="; z_c0=Mi4wQUdDQU5lTHRqQW9BVUlEbkpYbDZDaGNBQUFCaEFsVk5pZ1VIV0FCWmlnS1lzaVhvaEo2Yk1Od2pTSHMyU1VnWDJ3|1474263260|5c1631256f646345f7d2cebd0617fd5591b0af2d',
'Host':'www.zhihu.com',
'Pragma':'no-cache',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}    
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
        print img
        
#     all = json.loads(z.content)
    print 'x'
