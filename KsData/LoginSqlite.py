from KsData import SqliteCenter


class MetaSingleton(type):
    __instance={}
    def __call__(self, *args, **kwargs):
        if self not in MetaSingleton.__instance:
            MetaSingleton.__instance[self] = super(MetaSingleton,self).__call__()
        return MetaSingleton.__instance[self]

class loginsqlite(metaclass=MetaSingleton):
    def __init__(self):
        # self.SQL = SqliteCenter.SQLclass("Login.db")
        self.SQL = SqliteCenter.SQLclass("./KsData/Login.db")
    def AddPhone(self,tablename,phone,password):
        condition="phone="+phone
        tmpArr=self.SQL.GetData(tablename,condition)
        print(tmpArr)
        if tmpArr==[]:
            nature="(phone"
            value="('"+phone+"'"
            if password!="":
                nature=nature+",password"
                value=value+","+"'"+password+"'"
            nature=nature+")"
            value=value+")"
            self.SQL.AddData(tablename, nature, value)
        else:
            id=tmpArr[0][0]
            if password!="":
                self.SQL.Modify(tablename, "password='" + password+"'", "ID=" + str(id))
    def AddCode(self,tablename,phone,code):
        bb=self.SQL.Modify(tablename, "code='" + code+"'", "phone='" + phone+"'")
        rel="sucess"
        if not bb:
            rel="Fail"
        return rel
    def GetCode(self,tablename,phone):
        tmpArr = self.SQL.GetData(tablename, "phone='"+phone+"'")
        rel=""
        if tmpArr==[]:
            rel="未找到此号码，请检查"
        else:
            rel=tmpArr[0][3]
        return rel
    def GetStat(self,tablename,phone):
        tmpArr = self.SQL.GetData(tablename, "phone='"+phone+"'")
        rel=""
        if tmpArr==[]:
            rel="未找到此号码，请检查"
        else:
            rel=tmpArr[0][5]
        return rel
    def ModifyStat(self,tablename,phone,stat):
        tmpArr = self.SQL.GetData(tablename, "phone='" + phone + "'")
        if tmpArr!=[]:
            id=tmpArr[0][0]
            self.SQL.Modify(tablename, "stat='" + stat + "'", "ID=" + str(id))


# lq=loginsqlite()
# lq.AddPhone("Douyu","17359292429","l12345678")
