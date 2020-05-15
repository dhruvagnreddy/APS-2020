n=int(input())
t=1
for i in range(0,n):
    for j in range(0,i+1):
        print(t,end="")
    t=t+1
    print("\r")
