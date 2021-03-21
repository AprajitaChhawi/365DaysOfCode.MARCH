#User function Template for python3
import math
class Solution:
    def kThSmallestFactor(self, N , K):
        if N==1 and K==1:
            return 1
        l=[]
        for i in range(1,int(math.sqrt(N)+1)):
            if N%i==0:
                l.append(i)
        for i in range(len(l)-1,-1,-1):
            if l[i]!=N//l[i]:
                l.append(N//l[i])
        if K-1>len(l)-1:
            return -1
        return l[K-1]
            
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        
        ob = Solution()
        print(ob.kThSmallestFactor(N,K))
# } Driver Code Ends
