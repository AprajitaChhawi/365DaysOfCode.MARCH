#{ 
#Driver Code Starts
#Initial Template for Python 3


import math



 # } Driver Code Ends
#User function Template for python3

class Solution:    
    ##Complete this function
    def modInverse(self,a,m):
        for i in range(1,m):
            if (a*i)%m==1:
                return i
        return -1
        ##Your code here

#{ 
#Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        am=[int(x) for x in input().strip().split()]
        a=am[0]
        m=am[1]
        ob=Solution()
        print(ob.modInverse(a,m))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends
