#{ 
#Driver Code Starts
#Initial Template for Python 3


import math


 # } Driver Code Ends
#User function Template for python3
import math
class Solution:
    def isprime(self,i):
        if i==2 or i==3:
            return True
        if i%2==0 or i%3==0:
            return False
        for j in range(5,int(math.sqrt(i))+1,6):
            if i%j==0 or i%(j+2)==0:
                return False
        return True
    def exactly3Divisors(self,N):
        count=0
        for i in range(2,int(math.sqrt(N))+1):
            ob=Solution()
            if ob.isprime(i):
                count=count+1
        return count
            
        # code here

#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        ob=Solution()
        print(ob.exactly3Divisors(N))
        
        T-=1
    

if __name__=="__main__":
    main()
#} Driver Code Ends
