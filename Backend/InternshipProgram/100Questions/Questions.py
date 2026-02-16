

#  1) Find the Missing Number in an Array
# Given an array of n-1 integers ranging from 1 to n with no duplicates,
# find the missing number. The array contains distinct integers.
#?====================================================================================================

#*logic-1
def missing_num(lst):
    for val in range(1,len(lst)+1):
        if val in lst:
            # return val 
            pass
        else:
            return val
        
lst = [1,2,4,5]
print(missing_num(lst) )


#*logic -2
#* with the using of math 
# def missing_num(lst):
#     n = len(lst)+1
#     total  = n * (n + 1)//2
#     return total - sum(lst)

# lst  = [1,2,4,5]
# print(missing_num(lst))

#?====================================================================================================
# 2. Find the Duplicate Number
# Given an array containing n integers where each number is between 1
# and n-1, find the duplicate number.

# def duplicate_num(lst):
#     arr =[]
#     for val in lst:
#         if val not in arr:
#             arr.append(val)
#     print(arr)

# lst = [3, 1, 3, 4, 2]
# duplicate_num(lst)

# def duplicate_num(lst):
#     arr = []
#     for val in lst:
#         if val not in arr:
#             arr.append(val)
#         else:
#             return val 
            

# lst = [3, 1, 3, 4, 2]
# print(duplicate_num(lst) )


#?====================================================================================================
#! 3. Find the Majority Element (Moore’s Voting Algorithm)
# Given an array of size n, find the majority element (an element that
# appears more than n/2 times).
# Example:
# Input: [3, 3, 4, 2, 4, 4, 2, 4, 4]
# Output: 4


lst  = [3, 3, 4, 2, 4, 4, 2, 4, 4]
dict = {}
for val in lst:
    