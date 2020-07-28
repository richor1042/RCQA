
def sortdict(indict,model):
    tmparr = sorted(indict.items(), key=lambda x: x[1])
    posarr=[]
    negarr=[]
    for i in range(0,len(tmparr)):
        nowdata=tmparr[i]
        print(nowdata)
        if nowdata[1]<0:
            negarr.append(nowdata)
        else:
            posarr.append(nowdata)
    posarr.reverse()
    rel=None
    if model=="pos":
        rel=posarr
    else:
        rel=negarr
    return rel


fundsdict={}
fundsdict["aaa"]=12
fundsdict["aa1"]=6
fundsdict["bbb"]=-12
fundsdict["aab"]=-6
fundsdict["ccc"]=1

# f2=sorted(fundsdict.items(),key=lambda x:x[1])
#lambda为匿名函数 lambda x:x[1] 的意思是function(x) return x[1]
#sorted(list,key) key是排序依据
# print(f2)
# print(f2[1][1])
sortdict(fundsdict,"pos")


