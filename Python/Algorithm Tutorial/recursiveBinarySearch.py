def recursiveBinarySearch(list,target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursiveBinarySearch(list[midpoint+1:], target)
            else:
                return recursiveBinarySearch(list[:midpoint], target)
        
def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursiveBinarySearch(numbers,12)

verify(result)

result = result = recursiveBinarySearch(numbers,6)
verify(result) 