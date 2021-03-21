#User function Template for python3
import math
class Solution:
	def quadraticRoots(self, a, b, c):
	    d=b*b-4*a*c
	    e=[-1]
	    if d<0:
	        return e
	    if d==0:
	        a=math.floor((-b/(2*a)))
	        return a,a
	    a1=math.floor((-b+math.sqrt(d))/(2*a))
	    a2=math.floor((-b-math.sqrt(d))/(2*a))
	    return max(a1,a2),min(a1,a2)
	        
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        ob = Solution()
        ans = ob.quadraticRoots(a,b,c)
        if len(ans)==1 and ans[0]==-1:
            print("Imaginary")
        else:
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print()

# } Driver Code Ends
