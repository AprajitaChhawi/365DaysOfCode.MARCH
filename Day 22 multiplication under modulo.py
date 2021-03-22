#User function Template for python3

class Solution:
    def multiplicationUnderModulo(self,a,b):
        return (a*b)%1000000007
        '''
        :param a: given value of a
        :param b: given value of b
        :return: Integer , sum under modulo
        '''   
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a,b = map(int,input().strip().split())
        ob=Solution()
        print(ob.multiplicationUnderModulo(a,b))

# } Driver Code Ends
