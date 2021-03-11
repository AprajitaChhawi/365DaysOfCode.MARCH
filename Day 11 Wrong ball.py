try:
    t=int(input())
    while t:
        t=t-1
        n=input()
        t=len(n)
        count=0
        for i in range(t):
            if ((i+1)%2==0 and n[i]=='R'):
                count=count+1
            elif((i+1)%2==1 and n[i]=='B'):
                count=count+1
        print(count)
except Exception:
    pass;
