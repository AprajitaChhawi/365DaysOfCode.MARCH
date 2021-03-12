#your task is to complete this function
#Function should return the required answer
#You are not allowed to convert string to integer
def remainderWith7(str):
    return int(str)%7
    #Code here

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        print(remainderWith7(str))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
