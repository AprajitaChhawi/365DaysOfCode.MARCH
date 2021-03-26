#User function Template for python3

class Solution:
    def checkbit(self,pattern,arr,n):
        count=0
        for i in range(0,n):
            if((pattern&arr[i])==pattern):
                count=count+1
        return count
    #Complete this function
    # Function for finding maximum AND value.
    def maxAND(self, arr,n):
        res=0
        for bit in range(31,-1,-1):
            ob=Solution()
            count=ob.checkbit(res|(1<<bit),arr,n)
            if(count>=2):
                res=res|(1<<bit)
        return res
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxAND(arr,n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
