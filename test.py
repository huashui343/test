#-*-conding:utf-8-*-
import requests
import re
from lxml import etree

class CSRF:
    def __init__(self):
        self.head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
        self.url = 'https://www.speedo.com.cn/member/register/'


    def getcsrf(self):
        re = requests.get(self.url,headers = self.head)
        re.encoding = 'utf-8'
        html = etree.HTML(re.text)
        csrf = html.xpath('//meta[@name="_csrf"]//@content')
        csrfdata = csrf[0]
        return csrfdata
        
    def getcookie(self):
        re = requests.get(self.url,headers = self.head)
        re.encoding = 'utf-8'
        cookie = requests.utils.dict_from_cookiejar(re.cookies)
        return cookie

    def re(self,cookie):
        cookies = str(cookie)
        cookies = re.sub(r"{|}|'","",cookies)
        cookies = re.sub(r":","=",cookies)
        cookies = re.sub(r",",";",cookies)
        print (cookies)
        return cookies

class POST():
    def __init__(self):
        self.head = {
                    "Host":"www.speedo.com.cn",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
                    "Accept":"*/*",
                    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Referer":"https://www.speedo.com.cn/member/register/",
                    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                    "X-Requested-With":"XMLHttpRequest",
                    "Content-Length":"18",
                    "Connection":"close"
                     #'X-CSRF-TOKEN':'b3bb158a-7249-44a3-a365-caac59114e62'
                     #'Cookie':'route=bc7ef0fe794ac3a645beec38d264ea04; JSESSIONID=E78555033212BB12C57C24C8301FD306-n2.frontend_03'
                     }
        self.url = 'https://www.speedo.com.cn/member/checkLoginmobileAvailable.json'
        self.data = {
                    'mobile':'18725809370'
                    }
        self.proxies = {
            'https':'127.0.0.1:8080'
            }
        
    def yz(self,csrf2,cookies):
        self.head['X-CSRF-TOKEN'] = csrf2
        self.head['Cookie'] = cookies
        header = self.head
        re = requests.post(self.url,data = self.data,headers=header,proxies = self.proxies,verify=False)
        #print (self.head)
        print (header)

test = CSRF()
coo = test.getcookie()
cookie = test.re(coo) #cookie
csrf = test.getcsrf() #csrf

test2 = POST()
test2.yz(csrf,cookie)
