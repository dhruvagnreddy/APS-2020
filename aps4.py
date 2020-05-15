import itertools
n=int(input())
l1=[]
l2=[]
while(n>0):
    n=n-1
    x,y=map(int,input().split())
    l1.append(x)
    l2.append(y)
w=int(input())
#print(l1,l2)
result = [seq for i in range(len(l1), 0, -1) for seq in itertools.combinations(l1, i) if sum(seq) == w]
print(result)
