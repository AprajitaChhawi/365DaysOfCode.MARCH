

class Solution:
    #User function Template for python3
    
    
    '''
    	Your task is to return the lexicographically smallest 
    	max occuring charcter in given string.
    	
    	Function Arguments: s (given string)
    	Return Type: char or -1.
    	
    '''
    
    def getMaxOccurringChar(self,s):
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        t=0
        s=''
        for i in sorted(d.keys()):
            if d[i]>t:
                s=i
                t=d[i]
        return s
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        print(Solution().getMaxOccurringChar(s))
# } Driver Code Ends
