import sqlite3
import os
class SQLclass():
    conn=None
    c=None
    idnum=0
    def __init__(self,sqlname):
        self.db = sqlite3.connect(sqlname,check_same_thread = False)
        self.cursor = self.db.cursor()

    def execute(self, cmd):
        bb = True
        # print(cmd)
        try:
            # 执行sql语句
            bc = self.cursor.execute(cmd)
            # 提交到数据库执行
            self.db.commit()
            # print("执行成功")
        except Exception as e:
            print(e)
            # Rollback in case there is any error
            bb = False
            self.db.rollback()
        return bb
    def CreatTable(self,TableName,NatureType):
        cmd="CREATE TABLE "+TableName+"\n"+NatureType
        bb = self.execute(cmd)
        if bb:
            print("表格创建成功")
        else:
            print("表格创建失败")
        return bb
    def AddData(self, TableName, nature, value):
        cmd = "INSERT INTO " + TableName + nature + "\n" + "VALUES " + value
        bb = self.execute(cmd)
        if bb:
            print("添加成功")
        else:
            print("添加失败")
        return bb

    def DeleteData(self, TableName, condition):
        cmd = 'delete from ' + TableName + ' where ' + condition
        bb = self.execute(cmd)
        if bb:
            print("删除成功")
        else:
            print("删除失败")
        return bb

    def IsInside(self, TableName, condition):
        cmd = 'SELECT * FROM ' + TableName + ' where ' + condition
        bb = self.execute(cmd)

        if bb:
            # print("查询成功")
            results = self.cursor.fetchall()
            # print(results)
            if results == ()or results==[]:
                print("数据不存在")
                bb = False
        else:
            print("查询失败")
        return bb
    def GetData(self, TableName, condition,num=1):
        if condition=="":
            cmd = 'SELECT * FROM ' + TableName + " ORDER BY RANDOM() limit "+str(num)
        else:
            cmd = 'SELECT * FROM ' + TableName + ' where ' + condition+" ORDER BY RANDOM() limit "+str(num)
        bb = self.execute(cmd)
        results=""
        if bb:
            # print("查询成功")
            results = self.cursor.fetchall()
            # print(results)
            if results == ()or results==[]:
                print("数据不存在")
                bb = False
        else:
            print("查询失败")
        return results

    def Modify(self, TableName, SetValue, condition):
        cmd = 'UPDATE ' + TableName + ' SET ' + SetValue + ' where ' + condition
        # print(cmd)
        bb = self.execute(cmd)
        if bb:
            print("修改成功")
        else:
            print("修改失败")
        return bb
    def GetMaxID(self,Tablename):
        cmd='select max(id)  from '+Tablename
        bb = self.execute(cmd)
        results = ""
        if bb:
            # print("查询成功")
            results = self.cursor.fetchall()
            # print(results)
            if results == () or results == []:
                print("数据不存在")
                bb = False
        else:
            print("查询失败")
        return results
    def Close(self):
        self.db.close()

# sqlname='Wen.db'
# print(os.path.exists(sqlname))
# s1=SQLclass(sqlname)
# s1.GetMaxID("Sentence")
# s1.CreatTable("Type","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\ncontent           TEXT)")#类型
# s1.CreatTable("Play","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\nType           TEXT,\ncontent           TEXT)")#剧本
# s1.CreatTable("Prop","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\nType           TEXT,\ncontent           TEXT)")#道具
# s1.CreatTable("Role","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\nType           TEXT,\ncontent           TEXT)")#角色
# s1.CreatTable("Scene","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\nType           TEXT,\ncontent           TEXT)")#场景
# s1.CreatTable("Method","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\nType           TEXT,\ncontent           TEXT)")#方式
# s1.CreatTable("Post","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\nType           TEXT,\ncontent           TEXT)")#姿势
# s1.CreatTable("Stage","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\nType           TEXT,\ncontent           TEXT)")#阶段
# s1.CreatTable("Sentence","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\nType           TEXT,\nPlay           TEXT,\nProp           TEXT,\nRole           TEXT,\nScene           TEXT,\nMethod           TEXT,\nPost           TEXT,\nStage           TEXT,\ncontent           TEXT)")
# s1.CreatTable("Prop","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\ntype           TEXT    NOT NULL,\npassword           TEXT,\ncode           TEXT,\ntime           TEXT)")
# s1.CreatTable("YY","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\nphone           TEXT    NOT NULL,\npassword           TEXT,\ncode           TEXT,\ntime           TEXT)")
# s1.CreatTable("QiE","(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,\nphone           TEXT    NOT NULL,\npassword           TEXT,\ncode           TEXT,\ntime           TEXT)")
# s1.AddData("DidList","(did)","('f97a0a476fd8a526')")
# s1.AddData("COMPANY3","(NAME, AGE, ADDRESS)","('fuck1', 54, 'TestContent')")
# bb=s1.IsInside("COMPANY3","NAME='fuck2'")
# print(bb)

# #s1.creat()
# tmparr=[1,2,3]
# for id in tmparr:
#     s1.insert("fuckyour mother")
# rel= s1.getdata(2)
# print(rel)
# for id in range(4,6):
#     s1.insert("fuck")
# print("——————")
# rel= s1.getdata(2)
# print(rel)
# for id in range(4,6):
#     s1.insert("laji")
# print("——————")
# rel= s1.getdata(2)
# print(rel)