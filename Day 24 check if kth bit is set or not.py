#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends
#User function Template for python3

##Complete this code
#Function to check if Kth bit is set or not
class Solution:
    def checkKthBit(self, n,k):
        if k==0:
            return (1 & n)
        elif (n & (1<<(k))):
            return True
        else:
            return False
        #Your code here

#{ 
#Driver Code Starts.


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        obj = Solution()
        if obj.checkKthBit(n,k):
            print("Yes")
        else:
            print("No")
        
        T-=1

if __name__=="__main__":
    main()
#} Driver Code Ends
