#User function Template for python3
import math
class Solution:
    def sieveOfEratosthenes(self, N):
        temp=N+1
        ans=[]
        isprime=[True]*temp
        for i in range(2,int(math.sqrt(N)+1)):
            if isprime[i]==True:
                for j in range(2*i,N+1,i):
                    isprime[j]=False
        for i in range(2,N+1):
            if isprime[i]:
                ans.append(i)
        return ans
    	#code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends
