#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends
#User function Template for python3

class Solution:    
    #Compelte his function
    def termOfGP(self,A,B,N):
        a=A 
        return a*math.pow(B/A,N-1)
        #Your code here


#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        AB=[int(x) for x in input().strip().split()]
        A=AB[0]
        B=AB[1]
        
        N=int(input())
        ob=Solution()
        print(math.floor(ob.termOfGP(A,B,N)))
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends
