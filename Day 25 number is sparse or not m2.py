#User function Template for python3

class Solution:
    ##Complete this function
    # function to check if the number is sparse
    def isSparse(self,n):
        if(n==0 or n==1):
            return True
        temp=0
        while(n>0):
            k=n%2
            if k==1:
                temp=temp+1
                if(temp==2):
                    return False
            if k==0:
                temp=0
            n=n//2
        return True
        #Your code here 


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isSparse(n):
            print("1")
        else:
            print("0")
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
