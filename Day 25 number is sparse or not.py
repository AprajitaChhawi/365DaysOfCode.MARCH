#{ 
#Driver Code Starts
#Initial Template for Python 3

import math




    
 # } Driver Code Ends
#User function Template for python3

class Solution:
    ##Complete this function
    #function to find position of rightmost different bit
    def posOfRightMostDiffBit(self,m,n):
        co=1
        while((1&n)==(1&m)):
            co=co+1
            n=n>>1
            m=m>>1
        return co
        #Your code here

#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        ob=Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends
