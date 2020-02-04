# Author: Karan Singh Kochar
# Project title: simple coding challenges
# challenge: Array analysis for rolling equivalence


# arr1 = [1,2,3,4,5,6]
# arr2 = [5,6,1,2,3,4]
# here arr1 and arr2 is rolling equavalent
#
# arr1 = [1,2,3,4,5,6]
# arr2 = [5,6,1,2,4,3]
# here arr1 and arr2 is not rolling equavalent.
# Note: althought they have same elements, the order is not same.
def checkRolling(arr1, arr2):
    
    if len(arr1) != len(arr2):
        return 0
    
    elem1 = arr1[0]
    
    for i in range(len(arr1)):
        if arr2[i] == elem1:
            x = i
            j = 0
            while j < len(arr1):
                indexArr2 = (j + x) % len(arr2)
                if(arr1[j] != arr2[indexArr2]):
                    return 0
                j+=1
                i+=1
            return 1     
            

arr1 = [1,2,3,4,5,6]
arr2 = [5,6,1,2,3,4]

print(checkRolling(arr1, arr2))