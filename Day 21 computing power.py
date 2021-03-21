#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        if R==0:
            return 1
        ob=Solution()
        temp=ob.power(N,R//2)
        temp=temp*temp
        if R%2==0:
            return temp%1000000007
        else:
            return (N*temp)%1000000007
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
