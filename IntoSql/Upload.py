from urllib import parse
import requests
tablename="Sentence"
with open(tablename+".txt","r")as f:
    tmp=f.read()
# print(tmp)
# data=tmp
# for i in  range(0,10):
#     data=data.replace(str(i),"\n")

tmparr=tmp.split("\n")
# print(tmparr)
for sc in tmparr:
    data=sc
    # for i in range(0,10):
    #     data=data.replace(str(i),"")
    # data=data.replace(".","").replace("，","").replace(".","")
    print(data)
    if data!="":
        url="http://192.168.1.44:8000/fundnetadater/AddTableData?table="+tablename+"&data="+parse.quote(data)
        r=requests.get(url)


