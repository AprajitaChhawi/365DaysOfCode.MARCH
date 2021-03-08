# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1,str2):
    for i in str1:
        if i in str2:
            str1=str1.replace(i,"",1)
            str2=str2.replace(i,"",1)
    return len(str1)+len(str2)
    
    #add code here
    
    

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends
