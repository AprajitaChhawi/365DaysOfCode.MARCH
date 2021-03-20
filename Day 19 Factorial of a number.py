#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends
#User function Template for python3

class Solution:
    #You need to complete this function
    def factorial(self,N):
        if N==1 or N==0:
            return 1
        ob=Solution()
        return N*ob.factorial(N-1)
        #Your code here


#{ 
#Driver Code Starts.

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        ob=Solution()
        
        print(ob.factorial(N))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends
