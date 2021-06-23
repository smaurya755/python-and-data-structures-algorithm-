import keyword
print(keyword.kwlist)
print(id(None))
#1672214496
print('aab'>'aac')
print(ord('c'), ord('b'))
def linear_search(A, key):
    index = 0
    while index < len(A):
        if A[index]== key:
            return index
        index +=1
    return -1
print(linear_search([3, 12, 56, 7, 23], 12))
def binary_search(A, key):
    l = 0
    r = len(A)-1
    while l<r:
        m = (l+r)//2
        if A[m]== key:
            return m
        elif key< A[m]:
            l = l-1
        elif m>A[m]:
            r = r+1
    return -1

print(binary_search([3, 12, 56, 7, 23], 56))
print(binary_search([3, 12, 56, 7, 23], 12))
def binaryseaarch_recursive(A, key, l, r):
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binaryseaarch_recursive(A,key,l,mid-1)
        elif key > A[mid]:
            return binaryseaarch_recursive(A,key,mid+1,r)

A = [15, 21, 47, 84, 96]
found = binaryseaarch_recursive(A,17,0,4)
print('Result:', found)

def binary_recursive(A, key, l, r):
    if l>r:
        return -1
    else:
        m = (l+r)//2
        if key == A[m]:
            return m
        elif key < A[m] :
            binary_recursive(A, key, l, m-1)
        elif key > A[m]:
            binary_recursive(A, key, m+1, r)

A = [3, 12, 56, 7, 23]
print(binary_recursive(A, 23, 0, 4 ))
print(int(2.5))
#eval function: converts a data type in the form of string into its original data type
x = input()
y = input()



