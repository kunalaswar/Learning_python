# lst=[10,20,30,40,50,60]
# print(sum(lst))

# lst=[10,20,30,40,50,60]
# s=0
# for val in lst:
#     s=s+val
# print(s)    



#! program to accepting list of value  and  find  sum by  using redece() function 
import functools
def sumop(a,b):
    return(a+b)





print("Enter a list of value seperated by space :")
lst=[float(val) for val in input().split()]
res=functools.reduce(sumop,lst)    #NameError: name 'reduce' is not defined
print(res)




