# -*- coding:utf-8 -*-
import os
import xml.dom.minidom
import requests
import re
import json
import FundNetAdater





# 返回码
class ErrorCode(object):
    OK = "HTTP/1.1 200 OK\r\n"
    NOT_FOUND = "HTTP/1.1 404 Not Found\r\n"


# 将字典转成字符串
def dict2str(d):
    s = ''
    for i in d:
        s = s + i+': '+d[i]+'\r\n'
    return s

class Session(object):
    def __init__(self):
        self.data = dict()
        self.cook_file = None

    def getCookie(self, key):
        if key in self.data.keys():
            return self.data[key]
        return None

    def setCookie(self, key, value):
        self.data[key] = value

    def loadFromXML(self):
        import xml.dom.minidom as minidom
        root = minidom.parse(self.cook_file).documentElement
        for node in root.childNodes:
            if node.nodeName == '#text':
                continue
            else:
                self.setCookie(node.nodeName, node.childNodes[0].nodeValue)        

    def write2XML(self):
        import xml.dom.minidom as minidom
        dom = xml.dom.minidom.getDOMImplementation().createDocument(None, 'Root', None)
        root = dom.documentElement
        for key in self.data:
            node = dom.createElement(key)
            node.appendChild(dom.createTextNode(self.data[key]))
            root.appendChild(node)
        print(self.cook_file)
        with open(self.cook_file, 'w') as f:
            dom.writexml(f, addindent='\t', newl='\n', encoding='utf-8')

tts=0
class HttpRequest(object):
    RootDir = 'root'
    NotFoundHtml = RootDir+'/404.html'
    CookieDir = 'root/cookie/'
    sqlname = "./ksSpider/ks.db"
    s1 = None
    def __init__(self):
        self.method = None
        self.url = None
        self.protocol = None
        self.head = dict()
        self.Cookie = None
        self.request_data = dict()
        self.response_line = ''
        self.response_head = dict()
        self.response_body = ''
        self.session = None
        self.fundnetadater=FundNetAdater.fundnetadater()
        # print("调用HttpRequest构造函数")
        # self.appAdater.livesquare.ThreadStart()

    def passRequestLine(self, request_line):
        header_list = request_line.split(' ')
        self.method = header_list[0].upper()
        try:
            self.url = header_list[1]
            if self.url == '/':
                self.url = '/index.html'
            self.protocol = header_list[2]
        except Exception as e:
            print(e)

    def passRequestHead(self, request_head):
        head_options = request_head.split('\r\n')
        try:
            for option in head_options:
                key, val = option.split(': ', 1)
                self.head[key] = val
        except Exception as e:
            print(e)
            # print key, val
        if 'Cookie' in self.head:
            self.Cookie = self.head['Cookie']
    def cutreq(self,req):
        argsArr = req.split("&")
        param = {}
        for args in argsArr:
            tmp = args.split("=")
            param[tmp[0]] = tmp[1]
        return  param


    def passRequest(self, request):
        if request==None:
            return
        request = request.decode('utf-8',errors='ignore')
        if len(request.split('\r\n', 1)) != 2:
            return
        request_line, body = request.split('\r\n', 1)
        request_head = body.split('\r\n\r\n', 1)[0]     # 头部信息
        self.passRequestLine(request_line)
        self.passRequestHead(request_head)

        # 所有post视为动态请求
        # get如果带参数也视为动态请求
        # 不带参数的get视为静态请求
        if self.method == 'POST':
            self.request_data = {}
            try:
                request_body = body.split('\r\n\r\n', 1)[1]
                parameters = request_body.split('&')   # 每一行是一个字段
                req = self.url.split('?', 1)[1]
                s_url = self.url.split('?', 1)[0]
            except Exception as e:
                print(e)
            result=""
            # if s_url=="/proxypost":
            #     # http://47.106.231.199:8000/proxypost
            #     # url=http%3A%2F%2Fwww.baidu.com&headcookie=****&type=123&sig=asdsd
            #     p1 = poxyadater.poxynet()
            #     print("postadata=")
            #     print(request_body)
            #     result = p1.post(req)
            self.dynamicRequest(result)
        if self.method == 'GET':
            print("调用了get")
            if self.url.find('?') != -1:        # 含有参数的get
                self.request_data = {}
                req = self.url.split('?', 1)[1]
                s_url = self.url.split('?', 1)[0]
                parameters = req.split('&')
                result=""
                print(s_url)
                if "fundnetadater" in s_url:
                    result = self.fundnetadater.adater(s_url, req)
                print(result)
                self.dynamicRequest(result)
            else:
                self.staticRequest(HttpRequest.RootDir + self.url)

    # 只提供制定类型的静态文件
    def staticRequest(self, path):
        print("调用了静态get")
        print(path)
        result=""
        self.dynamicRequest(result)

    def processSession(self):
        self.session = Session()
        # 没有提交cookie，创建cookie
        if self.Cookie is None:
            self.Cookie = self.generateCookie()
            cookie_file = self.CookieDir + self.Cookie
            self.session.cook_file = cookie_file
            self.session.write2XML()
        else:            
            cookie_file = self.CookieDir + self.Cookie
            self.session.cook_file = cookie_file
            if os.path.exists(cookie_file):
                self.session.loadFromXML()                
            # 当前cookie不存在，自动创建
            else:
                self.Cookie = self.generateCookie()
                cookie_file = self.CookieDir+self.Cookie
                self.session.cook_file = cookie_file
                self.session.write2XML()                
        return self.session


    def generateCookie(self):
        import time, hashlib
        cookie = str(int(round(time.time() * 1000)))
        hl = hashlib.md5()
        hl.update(cookie.encode(encoding='utf-8'))
        return cookie

    def dynamicRequest(self, path):
        # 如果找不到或者后缀名不是py则输出404
        # print(path)
        f = open(HttpRequest.NotFoundHtml, 'r')
        self.response_line = ErrorCode.OK
        self.response_head['Content-Type'] = 'text/html'
        self.response_body = path


    def getResponse(self):
        # print("返回数据为")
        # print(self.response_body)
        return self.response_line+dict2str(self.response_head)+'\r\n'+self.response_body
