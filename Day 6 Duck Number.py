#User function Template for python3

class Solution:

    def check_duck(self, N):
        if N[0]!='0':
            if '0' in N:
                return 1
        return 0
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = input()

        solObj = Solution()

        if solObj.check_duck(N):
            print('YES')
        else:
            print('NO')
# } Driver Code Ends
