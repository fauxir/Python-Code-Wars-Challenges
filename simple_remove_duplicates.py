# Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.
# Example:

# For input: [3, 4, 4, 3, 6, 3]

#     remove the 3 at index 0
#     remove the 4 at index 1
#     remove the 3 at index 3

# Expected output: [4, 6, 3]

# More examples can be found in the test cases.

# Good luck!



def solve(arr):
    print("begining :",arr) 
    for i in range(0, len(arr)):
        for j in range(len(arr)-1, i, -1):
            if(arr[i] == arr[j]):
                x = arr.remove(arr[i])
                
    return x            


print(solve([3,4,4,3,6,3]))