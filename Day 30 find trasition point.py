
    # Perform Binary search
    while (lb <= ub):
        # Find mid
        mid = int((lb + ub) / 2)

        # update lower_bound if
        # mid contains 0
        if (arr[mid] == 0):
            lb = mid + 1

        # If mid contains 1
        elif (arr[mid] == 1):
            
            # Check if it is the 
            # left most 1 Return
            # mid, if yes
            if (mid == 0 \
                or (mid > 0 and\
                arr[mid - 1] == 0)):
                return mid

            # Else update 
            # upper_bound
            ub = mid-1
    
    return -1
    #Code here

#{ 
#  Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends
