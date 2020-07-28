from KsData import SqliteCenter
# import SqliteCenter
class MetaSingleton(type):
    __instance={}
    def __call__(self, *args, **kwargs):
        if self not in MetaSingleton.__instance:
            MetaSingleton.__instance[self] = super(MetaSingleton,self).__call__()
        return MetaSingleton.__instance[self]
class wensqlite(metaclass=MetaSingleton):
    def __init__(self):
        # self.SQL = SqliteCenter.SQLclass("Wen.db")
        self.SQL = SqliteCenter.SQLclass("./KsData/Wen.db")
    def AddData(self,TableName, data):
        data=dict(data)
        if TableName=="":
            return "fail"
        nature="("
        val="("
        for key in data:
            if data[key]!="":
                nature=nature+key+","
                val=val+"'"+data[key]+"',"
        nature=nature[:-1]+")"
        val=val[:-1]+")"
        rel=self.SQL.AddData(TableName,nature,val)
        return rel
    def GetMaxID(self,Tablename):
        rel=-1
        try:
            rel=self.SQL.GetMaxID(Tablename)[0][0]
        except Exception as e:
            pass
        print(rel)
        return rel
    def GetIDData(self,ID):
        condition = "ID="+str(ID)
        rel=self.SQL.GetData("Sentence",condition)
        return rel
    def GetData(self,TableName,data,num=1):
        data = dict(data)
        if TableName == "":
            return "fail"
        condition=""
        for key in data:
            if data[key]!="":
                # condition=condition+"("+key+"='"+data[key]+"'or "+key+" IS NULL) AND "
                condition = condition  + key + "='" + data[key] +  "' AND "
        try:
            condition=condition[:-5]
        except Exception as e:
            pass
        rel=self.SQL.GetData(TableName,condition,num)
        print(rel)
        return rel
    def ClearComb(self):
        ID=self.GetMaxID("Sentence")
        val="Comb=NULL"
        condition="ID="+str(ID)
        self.SQL.Modify("Sentence",val,condition)
# wl=wensqlite()
# testdata={
#     "Type":"测试",
#     "Role":"老师",
#     "Stage":"大学",
#     # "Scene":"办公室",
#     # "content":"在喝水"
# }
# # wl.AddData("Sentence",testdata)
# wl.GetData("Sentence",testdata,5)