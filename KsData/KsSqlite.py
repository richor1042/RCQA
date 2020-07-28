import sys
sys.path.append("..") #把上级目录加入到变量中
from KsData import SqliteCenter
import time

class kssqlite():
    def __init__(self):
        # self.SQL = SqliteCenter.SQLclass("KS.db")
        self.SQL = SqliteCenter.SQLclass("./KsData/KS.db")
        self.TableName = "TokenList"
        self.DidTable="DidList"
    def Adddata(self,data):
        # data={
        #     "phone":"16732046739",
        #     "Did":"b64a78a3bf961f9c",
        #     "Token":"6a0643a3ccfb4cd0bb97d7f4cf058ba2-1867566689",
        #     "Url":"http://apis2.gifshow.com/rest/n/feed/nearby?isp=CMCC&mod=samsung%28sm-j700f%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_b64a78a3bf961f9c&kpn=KUAISHOU&net=WIFI&app=0&oc=360APP%2C1&ud=1867566689&hotfix_ver=&c=360APP%2C1&sys=ANDROID_5.1.1&appver=6.5.6.9739&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1588815588605&ver=6.5&max_memory=192 HTTP/1.1",
        #     "Salt":"e5f10c17b06d634439bd1a5ebf65a786",
        #     "time":int(time.time())
        # }
        nature="("
        value="("
        for key in data:
            nature=nature+key+","
            if type(data[key])==str:
                value=value+"'"+str(data[key])+"',"
            else:
                value=value+str(data[key])+","
        nature=nature[:-1]+")"
        value=value[:-1]+")"
        # print(nature)
        # print(value)
        self.SQL.AddData(self.TableName,nature,value)
    def GetData(self,LimitTime):
        condition="Time<"+str(LimitTime)
        relList=self.SQL.GetData(self.TableName,condition)
        # print(relList)
        rel=""
        if len(relList)>0:
            rel=str(relList[0])
            id=relList[0][0]
            print(id)
            self.ResetTime(id)


        return rel
    def ResetTime(self,id):
        tt=str(int(time.time()))
        # print(tt)
        self.SQL.Modify(self.TableName, "Time="+tt,"ID="+str(id))
    def GetDid(self):
        relList = self.SQL.GetData(self.DidTable, "")
        # print(relList)
        rel=""
        if len(relList)>0:
            rel = relList[0][1]
            id = relList[0][0]

            # print(id)
            # self.SQL.DeleteData(self.DidTable,"ID="+str(id))
        # print("返回did"+rel)
        return rel
    def AddDid(self,did):
        nature="(did)"
        value="('"+did+"')"
        self.SQL.AddData(self.DidTable, nature, value)
        return "sucess"
    def DeleteDid(self,did):
        self.SQL.DeleteData(self.DidTable,"did='"+did+"'")
        return "sucess"



# kq=kssqlite()
# kq.DeleteDid("120b2cf3c932bc07")
# kq.ResetTime(10)
# kq.Adddata({})
# kq.GetDid()
