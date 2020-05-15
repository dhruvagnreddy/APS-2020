t=int(input())
while(t>0):
    t=t-1
    s=input()
    s=list(s)
    s.sort()
    c=[]
    r=[]
    for i in range(0,len(s)):
        a=0
        if(i not in c):
            for j in range(0,len(s)):
                if(s[i]==s[j]):
                    a=a+1
                    c.append(j)
            r.append(a)
    r.sort()
