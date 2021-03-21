#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        ans=[]
        a=A
        b=B
        while b!=0:
            temp=a%b
            a=b
            b=temp
        lcm=(A*B)//a
        return lcm,a
        
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends
