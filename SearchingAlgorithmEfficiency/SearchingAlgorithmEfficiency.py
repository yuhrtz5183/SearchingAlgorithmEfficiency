import time

#Binary Search Algorithm
def binarySearch(array, target):
    left, right = 0, len(array)-1
    while left <= right:
        middle = (left+right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1
#Linear Search Algorithm
def linearSearch(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
    return -1

array = range(1,10000000)
target = 1

#Getting the time for each algorithm
def timeSearch(search, array, target):
    start = time.perf_counter() #time.perf_counter() is faster and more accurate than time.time()
    result = search(array, target)
    end = time.perf_counter()
    execution = end - start
    return result, execution

#Binary Search with time
binaryResult, binaryTime = timeSearch(binarySearch, array, target)
if binaryResult != -1:   
    print(f"The array location of the target number {target} is in element",str(binaryResult))
    print(f"The time to execute the binary search algorithm is: {binaryTime:.10f} seconds")
else:
    print("WRONG NUMBER")

#Linear Search with time
linearResult, linearTime = timeSearch(linearSearch, array, target)
if linearResult != -1:
    print(f"\nThe array location of the target number {target} is in element",str(linearResult))
    print(f"The time to execute the linear search algorithm is: {linearTime:.10f} seconds")
else:
    print("WRONG NUMBER AGAIN")
