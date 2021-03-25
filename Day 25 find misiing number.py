#User function Template for python3


def MissingNumber(array,n):
    res=0
    for i in range(n+1):
        res=res^i
    for i in array:
        res=res^i
    return res
    # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=MissingNumber(a,n)
    print(s)
# } Driver Code Ends
