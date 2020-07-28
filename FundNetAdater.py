from  urllib import parse
import PlayerAdater
import os
import time
class fundnetadater():
    contents=[]
    playadter=PlayerAdater.playadter()
    WhiteList=[]
    def LoadWhiteList(self):
        filename="WhiteList.txt"
        with open(filename,"r")as f:
            tmp=f.read()
        self.WhiteList=tmp.split("\n")
        # print(self.WhiteList)
    def adater(self,url,req):
        rel=""
        if url == "/fundnetadater/PushContent":
            #http://47.106.231.199:8000/fundnetadater/PushContent?QQID=625860205&content=888888888888888
            rel= self.PushContent(req)
        if url == "/fundnetadater/GetContent":
            #http://192.168.1.44:8000/fundnetadater/GetContent?ID=123
            rel= self.GetContent(req)
        if url=="/fundnetadater/PrivateMsg":
            # http://192.168.1.44:8000/fundnetadater/PrivateMsg?QQID=123234234&msg=fuck
            rel=self.on_private_msg(req)
        if url=="/fundnetadater/AddTableData":
            # http://192.168.1.44:8000/fundnetadater/AddTableData?table=prop&data=%E7%B2%89%E7%AC%94
            rel=self.AddTableData(req)
        return rel
    def cutreq(self,req):
        argsArr = req.split("&")
        param = {}
        for args in argsArr:
            tmp = args.split("=")
            param[tmp[0]] = tmp[1]
        return  param
    def PushContent(self,req):
        print("添加内容")
        self.contents.append(req)
        return "sucess"
    def GetMessage(self):
        filename="C:\\Users\\Administrator\\Desktop\\CQA-tuling\\酷Q Air\\message.txt"
        tmp=""
        try:
            with open(filename,"r")as f:
                tmp=f.read()
        except Exception as e:
            pass
        if tmp!="":
            os.remove(filename)
            self.on_private_msg(tmp)
            print("已传输消息"+tmp)

    def GetContent(self,req):
        self.GetMessage()
        rel=""
        try:
            rel=self.contents.pop(0)
        except Exception as e:
            pass
        self.content=""
        return rel
    def on_private_msg(self,req):
        param=self.cutreq(req)
        qqid=param.pop("QQID","")
        msg=param.pop("msg","")
        if qqid=="":
            return "fail"
        self.LoadWhiteList()
        if not (qqid in self.WhiteList):
            return "No in WhiteList"
        print("收到"+qqid+"的消息:"+parse.unquote(msg))
        rel=self.playadter.AnanyzeMsg(parse.unquote(msg))
        tmparr=rel.split("\n")
        for tmp in tmparr:
            if tmp!="":
                tmpcont="QQID="+qqid+"&content="+parse.quote(tmp)
                self.contents.append(tmpcont)

        return "sucess"
    def AddTableData(self,req):
        param=self.cutreq(req)
        tablename=param.pop("table","")
        data=parse.unquote(param.pop("data",""))
        print(data)
        rel="fail"
        if tablename!="":
            rel=str(self.playadter.AddTableData(tablename,data))
        return rel
# f1=fundnetadater()



