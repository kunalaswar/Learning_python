
# sequence of a number 1 to n
# list=[1,2,3,3,5]
# find the missing element as well as duplicate element
# duplicate: 3
# missing:   4


# list1=[1,2,3,3,5]
# def find_duplicate_and_misssing(list1):
#     missing = 0
#     for i in range(len(list1)):
#         if i not in list1:
#             missing = i
#     for i in range(len(list1)):
#         for j in range(i+1,len(list1)):
#             if list1[i]==list1[j]:
#                 return list1[i],missing

# duplicate,missing = find_duplicate_and_misssing(list1)
# print("Duplicate : ",duplicate)
# print("Missing : ",missing)
