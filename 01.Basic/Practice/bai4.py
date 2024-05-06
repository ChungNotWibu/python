arr = [12,43,0,-21,69,43,13,-1]

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