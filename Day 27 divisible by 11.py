#User function Template for python3
class Solution:
	def divisibleBy11(self, S):
	    k=list(map(int,S.split()))
	    if sum(k)%11==0:
	        return 1
	    return 0
		# Your Code Here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		print (ob.divisibleBy11 (s)) 

# Contributed By: Pranay Bansal

# } Driver Code Ends
