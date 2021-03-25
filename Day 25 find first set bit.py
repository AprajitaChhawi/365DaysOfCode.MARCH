#{ 
#Driver Code Starts
#Initial Template for Python 3

import math



 # } Driver Code Ends
#User function Template for python3

class Solution:
    ##Complete this function
    #function to find position of first set bit in the given number
    # n is the given number.
    def getFirstSetBit(self,n):
        if n==0:
            return 0
        co=1
        while(n>0 and n%2==0):
            n=n//2
            co=co+1
        return co#Your code here

#{ 
#Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends
