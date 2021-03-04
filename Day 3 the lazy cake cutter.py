#User function Template for python3

class Solution:
	def maximum_Cuts(self, n):
	    return ((n*(n+1))//2)+1
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.maximum_Cuts(n)
		print(ans)
# } Driver Code Ends
