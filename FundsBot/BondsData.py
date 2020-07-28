import requests
import re
import time
class bondsdata():
    def GetBondData(self):
        url="http://data.eastmoney.com/kzz/default.html"
        r=requests.get(url)
        testdata=r.content
        xdata=testdata.decode('gbk','ignore')
        # print(xdata)
        pat='"SNAME":"(.*?)"'
        SNAME=re.findall(pat,xdata)
        pat=',"STARTDATE":"(.*?)T00:00:00"'
        STARTDATE=re.findall(pat,xdata)
        tt = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        print(STARTDATE)
        print(SNAME)
        rel=""
        for i in range(0,len(STARTDATE)):
            if STARTDATE[i]==tt:
                rel=rel+SNAME[i]+"\n"
        print(rel)
        return rel
# bd1=bondsdata()
# bd1.GetBondData()