"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

1) We are looking for a target value
2) we are looking at our array for 2 indices to add up to the value
3) so we look through our array store a indices to and its value into a dictionary and find the second number.


"""

def TwoSums(nums, target):
    numtoindex = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numtoindex:
            return [numtoindex[complement], i]
        ##numtoindex += nums[i] We can't use this in a dictionary
        numtoindex[num] = i

    else:
        return False 