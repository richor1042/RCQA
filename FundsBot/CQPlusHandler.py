# -*- coding:utf-8 -*-

import cqplus
import re
import time
import requests
from urllib import parse
num=0
class MainHandler(cqplus.CQPlusHandler):
    bb=False
    def cutreq(self,req):
        argsArr = req.split("&")
        param = {}
        for args in argsArr:
            tmp = args.split("=")
            param[tmp[0]] = tmp[1]
        return  param
    def handle_event(self, event, params):
        # global num
        # self.logging.debug("hello world")
        tt = time.strftime('%H:%M', time.localtime(time.time()))
        self.logging.debug("当前时间为:"+tt)
        if event=='on_private_msg':
            filename="message.txt"
            self.logging.debug("接收私聊到信息")
            # self.api.send_private_msg(params['from_qq'], params['msg'])
            # msg = params['msg']
            # msg=params.pop('msg',"")
            # qqid=params.pop('from_qq',"")
            # url = "http://47.106.231.199:8000/fundnetadater/PrivateMsg?QQID="+str(params['from_qq'])+"&msg="+parse.quote(params['msg'])
            data="QQID="+str(params['from_qq'])+"&msg="+parse.quote(params['msg'])
            self.logging.debug(data)
            with open(filename,"w")as f:
                f.write(data)
            # try:
            #     url="http://www.baidu.com"
            #     r = requests.get(url, timeout=5)
            #     testdata = r.content
            #     data = testdata.decode()
            #     data = parse.unquote(data)
            #     self.logging.debug("私聊请求成功")
            # except Exception as e:
            #     self.logging.debug(str(e))
            # self.logging.debug(params['from_qq'])
            # if msg=="1":
            #     self.api.send_private_msg(625860205, "nima")
            # else:
            #     self.api.send_private_msg(params['from_qq'],"fuck")
        elif event=='on_timer':
            url1 = "http://47.106.231.199:8000/fundnetadater/GetContent?ID=123"
            data1 = ""
            try:
                r = requests.get(url1, timeout=10)
                testdata = r.content
                data1 = testdata.decode()
                data1 = parse.unquote(data1)
                self.logging.debug("请求成功")
            except Exception as e:
                self.logging.debug("get失败")

            if data1 != "":
                backparam = self.cutreq(data1)
                try:
                    self.api.send_private_msg(int(backparam["QQID"]), backparam["content"])
                except Exception as e:
                    self.logging.debug("消息发送失败")
