#User function Template for python3
import math
class Solution:
    def largestPrimeFactor (self, N):
        temp=0
        for i in range(2,int(math.sqrt(N)+1)):
            while N%i==0:
                temp=i
                N=N//i
        if(temp==0):
            return N
        return max(N,temp)
        # code here
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends
