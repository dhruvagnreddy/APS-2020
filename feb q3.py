t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    a.insert(0,a[-1]) 
    a.append(a[1])
    a=[ a[i-1]+a[i+1] for i in range(1,n+1)]
    d=list(map(int,input().split()))
    maxi=[ d[i] for i in range(0,n) if(d[i]>a[i])]
    if(len(maxi)==0):
        print(-1)
    else:
        print(max(maxi))
        
