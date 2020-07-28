import os
import json
import re
import time
import KsSqlite
class userhand():
    def ReadFile(self):
        files = os.listdir('./raw_data')
        SaltRel=""
        TokenRel=""
        didRel=""
        for file in files:
            print(file)
            with open("./raw_data/"+file,"r",encoding='gb18030', errors='ignore')as f:
                tmp=f.read()
            # print(tmp)
            pat="did=ANDROID_(.*?)&"
            cont=re.findall(pat,tmp)
            # tmparr=tmp.split("\n\n")
            # jsontmp=tmparr[1]
            # jsondata = json.loads(jsontmp, strict=False)
            # # print(jsondata["token_client_salt"])
            # SaltRel=SaltRel+"'"+jsondata["token_client_salt"]+"'"+","
            # TokenRel=TokenRel+"'"+jsondata["token"]+"'"+","
            didRel=didRel+"'"+cont[0]+"'"+","
        print(didRel)
        # print(TokenRel)
    def WriteSql(self):
        kssqlite=KsSqlite.kssqlite()
        didArr = ['4524e6553870972e', '45b4546d6ca22cc0', '9fc285bbeae71210', 'b28f13ce16b9018c', 'c34bc3a51653af8c',
                  '067a136bb5b0ffa7', '84cc448e60cd7c8d', 'c7e9eb1fc7945cdc', '65f140fb08845b35', '104611bb33c582b4']
        SaltArr = ['b944e8c5a21483cce98fab4b6d50bd8b', '2e412d2126573325327aea77a4d49853',
                   'fe1a5a18763c7cd6328123235b0f72d1', '30d9fe6c730a9050b503478c93f4644e',
                   'ff94fd251d834306857cbb9d345b9d7a', '629841d7312d6bd0e91a1547aacbf954',
                   '57a869dd1ae352f5a7fb6253b65213d2', 'a7a6494f291820bf157b6c4203113611',
                   'b8b838cc0eee21257dfcb011c84c2d60', '092821d64f3f697f239f8c731a46744e']
        TokenArr = ['006242f87bc048fc8717a7dbced8fb59-1586609478', 'b79ec0b59bb14e499238119fb038baf5-1587029879',
                    '5b635e4f1e6443a58e663a1bf1bab9ff-1590109557', '2df5a507c9a848f48535bbab9344e751-1590689611',
                    '28a37cc763d343b7a594c4f50e04bdaa-1587190944', '765ef3e3466b4cdc949a7b07c394bab8-1588605668',
                    'fb8036e4d022412badc5d93dc63265e1-1589594568', 'db89246d028241b7b1ec77510c0d2f16-1590788905',
                    'fadc663ebb9144f7bb1e7fb8e6029434-1587226246', '988db0002aff4f75a6817de2fdfb726d-1587158334']
        for i in range(0,len(didArr)):
            data={
                "phone":"null",
                "Did":didArr[i],
                "Token":TokenArr[i],
                "Url":"http://apis2.gifshow.com/rest/n/feed/nearby?isp=CMCC&mod=samsung%28sm-j700f%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_b64a78a3bf961f9c&kpn=KUAISHOU&net=WIFI&app=0&oc=360APP%2C1&ud=1867566689&hotfix_ver=&c=360APP%2C1&sys=ANDROID_5.1.1&appver=6.5.6.9739&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1588815588605&ver=6.5&max_memory=192 HTTP/1.1",
                "Salt":SaltArr[i],
                "time":int(time.time())
            }
            kssqlite.Adddata(data)


uh1=userhand()
# uh1.WriteSql()
# uh1.ReadFile()