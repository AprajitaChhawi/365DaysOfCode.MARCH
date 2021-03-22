#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends
#User function Template for python3
import math
class Solution:
    def isPrime(self,N):
        if N==1:
            return False
        if N==2 or N==3:
            return True
        if N%2==0 or N%3==0:
            return False
        for j in range(5,int(math.sqrt(N))+1,6):
            if N%j==0 or N%(j+2)==0:
                return False
        return True
        # code here

#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        ob=Solution()
        if(ob.isPrime(N)):
            print("Yes")
        else:
            print("No")
        T-=1
    
    
if __name__=="__main__":
    main()
#} Driver Code Ends
