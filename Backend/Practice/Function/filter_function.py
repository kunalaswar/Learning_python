# def pos(val):
#     if(val>0):
#         return True
#     else:
#         return False




# print("Enter a value into list seperated by space")
# lst=[int(val) for val in input().split()]
# # print(lst)
# obj=filter(pos , lst ) 
# print(list(obj))

#?-----------------------------------------------------------------------------------------------------
#!wap to which will of numerical values and find odd numbers seperately & even seperately 
# lst=[int(val) for val in input().split()]
# obj1=list(filter(lambda val : val%2==0,lst))
# obj2=list(filter(lambda val : val%2!=0,lst))
# print("Even = ",obj1)
# print("Odd = ",obj2)

#?-----------------------------------------------------------------------------------------------------
#!wap program which will get those words whose lenght ranges between 2 and 3
# lst=[val for val in input().split()]
# obj1=list(filter(lambda val:len(val)==2 or len(val)==3,lst))
# # obj1=list(filter(lambda val:len(val)==3,lst))
# print(obj1)


#?-----------------------------------------------------------------------------------------------------
#!wap which will filter those words whose first letter and last letter is same
# lst=[val for val in input().split() ]
# obj1=list(filter(lambda val:val[0]==val[-1] and val!=val[::-1],lst))
# print(obj1)


#?-----------------------------------------------------------------------------------------------------

























