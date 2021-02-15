import math
tc=int(input())
while tc>0:
    N=int(input())
    W=list(map(int,input().split()))
    L=list(map(int,input().split()))
    index={}
    ans=0
    for i in range(1,N+1):
        index[i]=W.index(i)
    for i in range(2,N+1):
        val=0
        val1=index[i]
        val2=index[i-1] 
        if(val1<=val2):
            val=math.ceil((val2+1-val1)/(L[val1]))
        ans+=val
        index[i]+=val*(L[val1])
    print(ans)
    tc-=1    

