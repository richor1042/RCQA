import time
import requests
import re
class fundsdata():
    fundlist=[]

    def ReadFlie(self):
        filename="FundsList"
        with open(filename,"r")as f:
            fundlist=f.readlines()
        # print(fundlist)
        self.fundlist=fundlist
    def GetOneFundData(self,fundname):
        tt=int(time.time())
        # print(tt)
        url="http://fundgz.1234567.com.cn/js/"+fundname+".js?rt="+str(tt)
        r = requests.get(url)
        testdata = r.content
        xdata = testdata.decode()
        # print(xdata)
        pat='gszzl":"(.*?)"'
        rate=float(re.findall(pat,xdata)[0])
        pat='name":"(.*?)"'
        name = re.findall(pat, xdata)[0]
        rel={}
        rel[name]=rate
        # print(rel)
        return rel
    def GetAllFund(self):
        self.ReadFlie()
        ans={}
        for fund in self.fundlist:
            nowfun=fund.replace("\n","")
            tmp=self.GetOneFundData(nowfun)
            for key in tmp:
                ans[key]=tmp[key]
        print(ans)
        return ans
# fd1=fundsdata()
# fd1.ReadFlie()
# fd1.GetAllFund()