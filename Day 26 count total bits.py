#User function Template for python3

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        n=n+1
        power=2
        count=n//2
        while(power<=n):
            total=n//power
            count=count+(total//2)*power
            if(total & 1):
                count=count+(n%power)
            else:
                count=count+0
            power=power<<1
        return count # code here
        # return the count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends
