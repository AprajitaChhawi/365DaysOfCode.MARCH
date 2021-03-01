
class Solution:
    def find (self, N):
        return N+1
        
        # code here

#{ 
#  Driver Code Starts


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.find(N))
# } Driver Code Ends
