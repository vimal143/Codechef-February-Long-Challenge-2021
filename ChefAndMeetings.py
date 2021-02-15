def convert24(time): 
    if time[-2:] == "AM" and time[:2] == "12": 
        return "00" + time[2:-2] 
          
       
    elif time[-2:] == "AM": 
        return time[:-2]

    elif time[-2:] == "PM" and time[:2] == "12": 
        return time[:-2] 
          
    else: 
        return str(int(time[:2]) + 12) + time[2:6] 

tc=int(input())
while tc>0:
    ans=""
    P=input()
    N=int(input())
    for i in range(0,N):    
        LR=input()
        L=LR[:8]
        R=LR[9:17]
        ActP=convert24(P)
        L24=convert24(L)
        R24=convert24(R)
        Lreal=int(L24.replace(":",""))
        Rreal=int(R24.replace(":",""))
        Preal=int(ActP.replace(":",""))
        if(Lreal<=Preal and Rreal>=Preal):
            ans+="1"
        else:
            ans+="0"      
    
    
    print(ans)
    tc-=1

