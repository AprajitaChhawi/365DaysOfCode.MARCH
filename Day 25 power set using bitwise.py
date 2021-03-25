#User function Template for python3
import math
class Solution:
	def AllPossibleStrings(self, s):
	    ntemp=len(s)
	    l1=[]
	    temp=int(math.pow(2,ntemp))
	    for i in range(0,temp):
	        l=""
	        for j in range(0,ntemp):
	            if(i&(1<<j)!=0):
	                l=l+s[j]
	        l1.append(l)
	    l1.pop(0)
	    l1.sort()
	    return l1
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends
