t=int(input())
while t:
    t=t-1
    k=''
    n1=[]
    n2=[]
    n,s=input().split()
    n1[:0]=n
    n2[:0]=s
    k1=len(n1)
    k2=len(n2)
    for i in range(min(k1,k2)):
        k=k+n1.pop(0)
        k=k+n2.pop(0)
    if n2:
        while n2:
            k=k+n2.pop(0)
    if n1:
        while n1:
            k=k+n1.pop(0)
    print(k)
    
