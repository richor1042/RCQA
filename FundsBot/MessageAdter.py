import smtplib
from email.mime.text import MIMEText
import time
from urllib import parse
import requests
class QQmail():
    def __init__(self):
        self.msg_from = '625860205@qq.com'  # 发送方邮箱
        self.passwd = 'zccmhvrrswxmbegc'  # 填入发送方邮箱的授权码
        self.FundList={}
        self.BondList={}
        self.SetQQandTime()
    def GetTotalTime(self):
        timearr=[]
        for key in self.FundList:
            if  not(key in timearr):
                timearr.append(key)
        for key in self.BondList:
            if not (key in timearr):
                timearr.append(key)
        return timearr
    def GetFundTime(self):
        timearr = []
        for key in self.FundList:
            if not (key in timearr):
                timearr.append(key)
        return timearr
    def GetBondTime(self):
        timearr = []
        for key in self.BondList:
            if not (key in timearr):
                timearr.append(key)
        return timearr
    def BuitDict(self,data):
        tmparr=data.split("\n")
        reldict={}
        for tmp in tmparr:
            if tmp.find(":")>0:
                tmparr2=tmp.split(" ")
                key=tmparr2[0]
                val=tmparr2[1].split("/")
                reldict[key]=val
        return reldict
    def SetQQandTime(self):
        filename="QQListSet.txt"
        with open(filename,"r")as f:
            tmp=f.read()
        # print(tmp)
        tmparr=tmp.split("\n\n\n")
        self.FundList=self.BuitDict(tmparr[0])
        print(self.FundList)
        self.BondList=self.BuitDict(tmparr[1])
        print(self.BondList)

    def sendmail(self,msg_to,subject,content):
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = self.msg_from
        msg['To'] = msg_to
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(self.msg_from, self.passwd)
        s.sendmail(self.msg_from, msg_to, msg.as_string())
        print("发送成功")
    def ReadMail(self):
        filename = "MailList"
        with open(filename, "r")as f:
            Maillist = f.readlines()
        # print(fundlist)
        self.Maillist = Maillist
    def ReadQQID(self):
        filename = "QQIDList"
        with open(filename, "r")as f:
            QQIDlist = f.readlines()
        # print(fundlist)
        self.QQIDlist = QQIDlist
    def ReadQQIDList(self,DictName,TargetTime):
        if DictName=="Fund":
            self.QQIDlist = self.FundList[TargetTime]
        else:
            self.QQIDlist = self.BondList[TargetTime]
    def PushConten(self,QQID,data):

        url="http://47.106.231.199:8000/fundnetadater/PushContent?QQID="+QQID+"&content="
        content=parse.quote(data)
        print(content)
        url=url+content
        print(url)
        try:
            r=requests.get(url)
            testdata=r.content
            xdata = testdata.decode()
            print(xdata)
            print("请求成功")
        except Exception as e:
            print("get失败")

    def SendAllMail(self,content,subject,DictName,TargetTime):
        # self.ReadMail()
        self.ReadQQIDList(DictName,TargetTime)
        # subject="基金提醒"
        tt=time.strftime('%Y-%m-%d', time.localtime(time.time()))
        subject=tt+subject
        print(subject)
        QQcontent=subject+"\n"+content
        conts=QQcontent.split("\n")
        contsplit=[]
        tmp=""
        for i in range(0,len(conts)):
            if i==9:
                contsplit.append(tmp)
                tmp=conts[i]+"\n"
            else:
                tmp=tmp+conts[i]+"\n"
        if tmp!="":
            contsplit.append(tmp)
        # QQcontent=parse.quote(QQcontent)
        print(QQcontent)
        for QQID in self.QQIDlist:
            nowid=QQID.replace("\n","")
            if nowid!="":
                for tmpcont in contsplit:
                    self.PushConten(nowid, tmpcont)
        # for mail in self.Maillist:
        #     nowmail=mail.replace("\n","")
        #     self.sendmail(nowmail,subject,content)
        #     time.sleep(1)
QQ1=QQmail()
# QQ1.SetQQandTime()
rel=QQ1.GetTotalTime()
print(rel)
# QQ1.SendAllMail("提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功提醒成功")
