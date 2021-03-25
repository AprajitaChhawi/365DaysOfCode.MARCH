#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        res=0
        res1=0
        res2=0
        for i in Arr:
            res=res^i
        a=res&(~(res-1))
        for i in Arr:
            if i&a:
                res1=res1^i
            else:
                res2=res2^i
        return max(res1,res2),min(res1,res2)
        # code here


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends
