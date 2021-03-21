#User function Template for python3
import math
class Solution:
    def facDigits(self,N):
        x=0
        if N<=1:
            return 1
        x = ((N * math.log10(N / math.e) + math.log10(2 * math.pi * N) /2.0))
        return math.floor(x)+1
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.facDigits(N))
# } Driver Code Ends
