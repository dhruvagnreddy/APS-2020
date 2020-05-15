import sys
def decimalToBinary(n):  
    res= bin(n).replace("0b", "")
    print(len(str(res)))
def hexaToBinary(n):
    res = bin(int(n,16)).zfill(8)
    print(len(str(res))-2)
def octToBinary(n):
    res= bin(int(n)).replace("0b", "")
    print(len(str(res)))
q=int(input())
while(q>0):
    q=q-1
    n,b=(input().split())
    b=int(b)
    if(b==2):
        n=int(n)
        print(len(str(n)))
    elif(b==8):
        n=int(n)
        octToBinary(n)
    elif(b==10):
        n=int(n)
        decimalToBinary(n)
    elif(b==16):
        hexaToBinary(n)
    else:
        sys.exit(0)
               
