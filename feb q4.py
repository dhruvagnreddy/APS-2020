t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    print(sum(l)-n)
    
