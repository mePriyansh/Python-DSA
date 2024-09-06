import array

arr = array.array('i', [1, 2, 3, 4, 5])

def traverse(arr):
    for i in arr:
        print(i)
        
traverse(arr)