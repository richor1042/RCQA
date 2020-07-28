from KsData import WenSqlite

class MetaSingleton(type):
    __instance={}
    def __call__(self, *args, **kwargs):
        if self not in MetaSingleton.__instance:
            MetaSingleton.__instance[self] = super(MetaSingleton,self).__call__()
        return MetaSingleton.__instance[self]

class playadter(metaclass=MetaSingleton):
    wensqlite=WenSqlite.wensqlite()
    def __init__(self):
        self.data={
            "Type":"",
        }
        self.typedata = {
            "类型": "Type",
        }
        self.tmpcontenr=[]
        self.mode=""
        self.combtimes=0
    def AddTableData(self,Tablename,data):
        nowdict={
            "content":data
        }
        rel=self.wensqlite.AddData(Tablename, nowdict)
        return rel
    def GetIDData(self,ID):
        tmparr=self.wensqlite.GetIDData(ID)
        rel=""
        if len(tmparr)>0:
            comb=tmparr[0][len(tmparr[0])-2]
            rel=tmparr[0][len(tmparr[0])-1]
            if comb!=None and comb!="":
                rel=rel+" comb "+str(comb)
        return rel
    def CombMsg(self,msg):
        if msg == "退出comb模式":
            self.mode = ""
            self.combtimes=0
            self.wensqlite.ClearComb()
            return "退出成功"

        tablename="Sentence"
        maxid=int(self.wensqlite.GetMaxID(tablename))
        if maxid<0:
            return "comb失败"
        comb=str(maxid+2)
        tmpdict={}
        for key in self.data:
            tmpdict[key]=self.data[key]
        # print(self.combtimes)
        # print(tmpdict)
        tmpdict["Comb"]=comb
        self.combtimes=self.combtimes+1
        tmpdict["content"] = msg
        self.wensqlite.AddData("Sentence", tmpdict)
        return "comb成功"

    def AnanyzeMsg(self,msg):
        rel="数据格式错误"

        if msg.find("设置")>-1:
            self.SetMsg(msg)
            rel="设置成功"
        else:
            if msg.find("，，，") > -1:
                bb = True
                tmp = msg.split("，，，")
                data = tmp[0]
                data2 = tmp[1]
                print(tmp)
                if data2 != "":
                    print("添加数据")
                    print(data2)
                    nowdict = self.data
                    nowdict["content"] = data2
                    self.wensqlite.AddData("Sentence", nowdict)
                    rel="添加成功"
            if msg.find("获取")>-1:
                print("开始获取数据")
                num=1
                try:
                    num=int(msg[4:])
                except Exception as e:
                    pass
                # print(num)
                tablekey=msg[2:4]
                # print(tablekey)
                tablename=""
                nowdict={}
                nowdict["Type"]=self.data["Type"]
                if tablekey=="内容":
                    tablename="Sentence"
                    nowdict=self.data
                else:
                    tablename=self.typedata.get(tablekey,"")
                # print(tablename)
                if tablename=="":
                    return "fail"
                backrel=self.wensqlite.GetData(tablename,nowdict,num=num)
                rel=" "
                for tu in backrel:
                    comb=tu[len(tu)-2]
                    if comb!=""and comb !=None:
                        rel = rel + tu[len(tu) - 1] +"comb "+str(comb)+ "\n"
                    else:
                        rel=rel+tu[len(tu)-1]+"\n"
                # print(rel)
            if msg.find("清除")>-1:
                print("开始清除")
                tablekey = msg[2:4]
                print(tablekey)
                if tablekey=="所有":
                    for key in self.data:
                        self.data[key]=""
                else:

                    tablename=self.typedata.get(tablekey,"")
                    print(tablename)
                    self.data[tablename]=""
                rel="清除成功"
            if msg.find("跳转")>-1:
                ID=0
                try:
                    ID=int(msg[2:])
                except Exception as e:
                    pass
                if ID>0:
                    rel=self.GetIDData(ID)
            if self.mode == "comb" and rel=="数据格式错误":
                rel = self.CombMsg(msg)
                return rel
            if msg=="进入comb模式":
                self.mode="comb"
                self.combtimes=0
                rel="进入comb模式成功"
        return rel


    def SetMsg(self,msg):
        data = ""
        data2 = ""
        # print(msg.find("，，，"))
        if msg.find("，，，")>-1:
            bb = True
            tmp = msg.split("，，，")
            data = tmp[0]
            data2 = tmp[1]
            # print(tmp)
        else:
            # print("设置了data")
            data = msg
            bb = False
        # print(data)
        tmparr = data.split("，")
        # print(tmparr)
        for tmpkey in tmparr:
            tmp2 = tmpkey.replace("设置","").split("为")
            if len(tmp2)<2:
                return
            key = self.typedata.get(tmp2[0], "")
            if key != "":
                self.data[key] = tmp2[1]
        # print(self.data)


