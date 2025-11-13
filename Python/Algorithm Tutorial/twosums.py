"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

1) We are looking for a target value
2) we are looking at our array for 2 indices to add up to the value
3) so we look through our array store a indices to and its value into a dictionary and find the second number.


"""

def twoSum(nums, target):
    numtoindex = {} # This is to store the data from the nums list.
    for i, num in enumerate(nums): # This is to loop through the nums lists for the index and the value.
        complement  = target - num # This is to find the missing half of the number.
        if complement in numtoindex: # is to check if we have the complement number in the numtoindex dictionary,
            #if our number is 2 we are looking for a 7. But our current dictionary is empty thus there is no number so we just store it in first.
            #so we move on to the second number which is 7, we will then repeat the process again.
            return [numtoindex[complement], i]
        
        numtoindex[num]= i




nums =[2,7,11,15,12,17,20]
target = 29

print(twoSum(nums,target))