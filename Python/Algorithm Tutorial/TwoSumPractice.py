def twosums(nums,target):
    numtoindex={}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numtoindex:
           return True
        
        numtoindex[num] = i
    else:
        return False


nums = [1,2,3,4,5,10,15]
target = 90

print(twosums(nums,target))