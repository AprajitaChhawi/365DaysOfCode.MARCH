#User function Template for python3
import math
class Solution:
    def isPrime(self,i):
        if i==1:
            return False
        if i==2 or i==3:
            return True
        if i%2==0 or i%3==0:
            return False
        for j in range(5,int(math.sqrt(i)+1),6):
            if i%j==0 or i%(j+2)==0:
                return False
        return True
    def largestPrimeFactor (self, N):
        temp=0
        for i in range(2,int(math.sqrt(N)+1)):
            ob=Solution()
            if ob.isPrime(i):
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
