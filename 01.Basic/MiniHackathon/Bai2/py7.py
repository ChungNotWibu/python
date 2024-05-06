arr = [5, 1, 8, 92, -1, 30]

print("Original list:")
print("5 1 8 92 -1 30")

def bSort(arr):
    n = len(arr)
    s = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                s = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]        
        if not s:
            return

bSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i] , end = " ")
print()