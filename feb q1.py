from math import gcd
t=int(input())
while(t>0):
    t=t-1
    n,a,b,k=map(int,input().split())
    y=(a*b)/gcd(a,b)
    if(b>a):
        a,b=b,a
    if(a%b!=0):
        ad1=(n//a)-(n//y)
        ad2=(n//b)-(n//y)
        total=ad1+ad2
    else:
        total=(n//b)-(n//a)
    if(total>=k):
        print('Win')
    else:
        print('Lose')
    
    #l=[]
    #l=[ i for i in range(1,n+1)]
    #l=[ l[i] for i in range(0,n) if((l[i]%a==0 and l[i]%b!=0) or(l[i]%b==0 and l[i]%a!=0))]
        
