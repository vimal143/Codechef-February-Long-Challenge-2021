tc=int(input())
while tc>0:
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    max=A[N-1]
    min=A[0]
    ans=max-min
    print(ans*2)
    tc-=1
    