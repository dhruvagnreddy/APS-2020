
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    l=[]
    while(n>0):
        n=n-1
        s=input()
        l.append(set(s))
    inter=set.intersection(*l)
    print(len(inter))
