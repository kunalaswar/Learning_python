# resursion : calling function again and again until some condition get satisfied 
# stack will be Created into the stack segment 
# stack standard routines:
# 1.push : recursive calls
# 2.pop : when recursion call execution done it started returnning  the value thatyy value is getting pop up 


#*  factorical in recursion
def factorical(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorical(n-1)
    
print(factorical(5))    
# #But
# print(factorical(50000))
# print(factorial(-5))


#! how to habdle the boundary case for large number (recursion error)
#!  we want first 20 digit  of the factorial in the recirsion
#! for negative number there is no factorial :handle it 


#! 2) number =10
#! want to sum of first 10 natural number 

# after appling the repetative step at the End automatically we are getting the anchor step



# def sum_naturalnum(n):
#     if n ==0 :
#         return 0

#     else:
#         return n +sum_naturalnum(n-1)
# print(sum_naturalnum(10))    
# print(sum_naturalnum(-5))    
#! Exception for this above question
    
# sum = 0
# for val in range(1,11):
#     sum = sum+val
# print(sum)  


#^  Divide and conquer stratery is the recursive approach
#^  backtracking 
#^  DP (dynamic programming)

# def minmaxproblem(list1,low,high):
#     if low==high:
#         return  list1[low],list1[high]
#     elif high ==low+1:
#         if list1[low]>list1[high]:
#             return list1[high],list1[low]
#         else:
#             return list1[low],list1[high]
        
#     else:
#         mid = (low + high )//2
#         min1,max1 = minmaxproblem(list1,low,mid)
#         min2,max2 = minmaxproblem(list1,mid+1,high)
#         original_min = minimum(min1,min2)
#         original_max = maximum(max1,max2)
#         return  original_min,original_max
# def minimum(a,b):
#     if a<b:
#         return a
#     else :
#         return b
# def maximum(c,d)    :
#     if c>d:
#         return c
#     else:
#         return d
# list1 = [23,8,91,-9,0,23,16,-2]    
# low = 0
# high =  len(list1)-1
# print(minmaxproblem(list1,low,high))


#! find out common Element between two list

list1 = [34,0,91,24,-50]
list2 = [0,1,2,3,24,-50]

