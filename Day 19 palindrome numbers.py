#User function Template for python3

class Solution:
	def is_palindrome(self, n):
	    res=list(map(int,str(n)))
	    temp=len(res)
	    for i in range(0,(temp//2)+1):
	        if res[i]!=res[temp-i-1]:
	            return "No"
	    return "Yes"
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends
