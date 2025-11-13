# Step 1: Define a function that takes in a string 's'
def longest_substring_without_repeating_characters(s):
    
    # Step 2: Create a variable to store the longest substring length
    longest = 0
    
    # Step 3: Create a left pointer (start of window)
    left = 0
    
    # Step 4: Create a dictionary to count how many times each character appears
    counter = {}
    
    # Step 5: Loop through each character in the string using a right pointer
    for right in range(len(s)):
        char = s[right]
        
        # Step 6: Increase the count of this character in the dictionary
        counter[char] = counter.get(char,0  ) + 1
        
        # Step 7: If we have a duplicate (count > 1), move the left pointer
        while counter[char] > 1:
            left_char = s[left]
            counter[left_char] -= 1
            left += 1
        
        # Step 8: Update longest if the current window is longer
        longest = max(longest, ___ - ___ + 1)
    
    # Step 9: Return the result
    return ___