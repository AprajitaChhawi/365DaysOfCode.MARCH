#User function Template for python3
'''
Function Arguments :
		@param  : n (given number)
		@return : list of all the binary numbers till n.
'''
def generate(N):
    q=['1']
    l=[]
    while len(q)<=N:
        s=q.pop(0)
        l.append(s)
        q.append(s+'0')
        q.append(s+'1')
    return l
    # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by :  Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        res = generate(n)
        for i in range (len (res)):
            print (res[i], end=" ")
        print()
# } Driver Code Ends
