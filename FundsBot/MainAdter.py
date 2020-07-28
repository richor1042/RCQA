import FundsData
import MessageAdter
import time
import datetime
import BondsData
class mainadter():
    def __init__(self):
        self.FundsData=FundsData.fundsdata()
        self.QQmail=MessageAdter.QQmail()
        self.BondsData=BondsData.bondsdata()

    def sortdict(self,indict, model):
        tmparr = sorted(indict.items(), key=lambda x: x[1])
        posarr = []
        negarr = []
        for i in range(0, len(tmparr)):
            nowdata = tmparr[i]
            print(nowdata)
            if nowdata[1] < 0:
                negarr.append(nowdata)
            else:
                posarr.append(nowdata)
        posarr.reverse()
        rel = None
        if model == "pos":
            rel = posarr
        else:
            rel = negarr
        return rel
    def SendData(self,content):
        self.QQmail.SendAllMail(content)
        return "success"
    def StartAnalyze(self,TargetTime):
        relList=self.FundsData.GetAllFund()
        posarr=self.sortdict(relList,"pos")
        negarr=self.sortdict(relList,"neg")

        rel1="**********跌幅排行*********\n"
        for data in negarr:
            rel1=rel1+data[0]+":"+str(data[1])+"\n"

        rel2 = "**********涨幅排行**********\n"
        for data in posarr:
            rel2 = rel2 + data[0] + ":" + str(data[1]) + "\n"
        print(rel2)
        self.QQmail.SendAllMail(rel1,"基金提醒","Fund",TargetTime)
        self.QQmail.SendAllMail(rel2,"","Fund",TargetTime)
    def StartGetBonds(self,TargetTime):
        rel=self.BondsData.GetBondData()
        if rel!="":
            self.QQmail.SendAllMail(rel,"可申购债券","Bond",TargetTime)
    def Chektime(self):
        TargetTimes=self.QQmail.GetTotalTime()
        print(TargetTimes)
        FundTimes=self.QQmail.GetFundTime()
        BondTimes=self.QQmail.GetBondTime()
        tt = time.strftime('%H:%M', time.localtime(time.time()))
        print(tt)
        bb=False
        while True:
            print("延时")
            time.sleep(59)
            tt = time.strftime('%H:%M', time.localtime(time.time()))
            wd = datetime.datetime.now().weekday()
            if wd<5:
                if (tt in TargetTimes)and(not bb):
                    if tt in FundTimes:
                        print("开始获取基金信息")
                        self.StartAnalyze(tt)
                    if tt in BondTimes:
                        print("开始获取债券信息")
                        self.StartGetBonds(tt)
                    bb=True
                else:
                    bb=False
md1=mainadter()
md1.Chektime()
# md1.StartAnalyze()