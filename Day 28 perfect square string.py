import math
for t in range(int(input())):
    s=input()
    total=0
    for i in s:
        total+=ord(i)
    n=int(math.sqrt(total))
    if n*n==total:
        print("1")
    else:
        print("0")
