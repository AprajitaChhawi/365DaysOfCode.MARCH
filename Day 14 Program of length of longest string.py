t=int(input())
while t:
    t=t-1
    n=list(map(str,input().split()))
    l=0
    for i in n:
        if len(i)>l:
            l=len(i)
    print(l)
    
