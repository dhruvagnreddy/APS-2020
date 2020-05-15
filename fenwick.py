def update(index,val):
    for i in range(index,n+1):
        i=i+(i&i)
        BIT[i]+=val
    print(BIT[i])
        
def query(x):
    qsum=0
    for i in range(x,0):
        i=i-(i&-i)
        qsum+=BIT[i]
    print(qsum)

BIT=[0 for i in range(0,1000)]
n=10
BIT=[1,2,3,4,5,6,7,8,9,10]
update(3,9)
query(4)
print
