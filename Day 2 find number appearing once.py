#User function Template for python3
class Solution:
    def search(self, A, N):
        d={}
        for i in A:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        #print(d)
        for i in d.keys():
            if d[i]==1:
                return i
        # your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends
