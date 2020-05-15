n=int(input())
l=list(map(int,input().split()))
k=int(input())
if(k>n):
    print(*l)
else:
    minl=sorted(l)[k-1]
    l=l[-minl:] + l[:-minl]
    print(*l)
#maxl=sorted(l,reverse=True)[k-1]
#ind=l.index(maxl)
#print(minl,maxl,ind)
