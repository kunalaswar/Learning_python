
# we can tackle Every Question with the Help of Recursion 

# how to write a function in python
#1.function  def
#2.function calling

# def my_fun(arg):
#     body

# my_fun(arg)    

# Recursion

#* 1. anchor step or stop step
# => where we need to stop calling the function

#* 2. recursive step or inductive step
# => repetative statements (which statement we need to execute repetedaly that we will keep in recursive step )

# Memory is the collection of segment
# lst = [1,2,3]----> heap segment


# 1.code segment
# => it is read only purpose -- we cant change anythings
# 2.data segment
# => it will contains the global varible,static varible class varible global function
# 3.stack segment
#   => IMP ===>local varible,recursive function call,stack 
# 4.heap segment
# => all the collection datatypes in like a data Structure in python is created in the heap segment
# because  it is dynamic in Nature 

# whenEver we writting a recursive stack will be Created in the stack    segemnt implicitly

#* stack : Linear DS storing the Element into the linear fashion 
#* stack is the logical Data Structure 
#* physical it will stored in the form of list in python 

#todo - principle  LIFO and FILO:
#^1. push :inserting the Element into the stack
#^2. pop : removing the Element into the stack

#todo - recursive code :
#^1. push :inserting all the recursive call into the stack . whenEver we call recursive function it will get push into the stack ===> winding phase

#^2. pop : the recursive function call execution is over will start returning the value that    value will get pop ===> unwinding phase

# function  call will be stored inside the stack in the form of activation record or stack frame



# max size of stack = size of stack segment

# find the multiplication of the two number 
 

# def recursive_mul(a,b):
#     if b==0:
#         return 0
#     else:
#         return a + recursive_mul(a,(b-1))
# print(recursive_mul(6,4)) 



#! 09-04-2025

# recursive division  
# def recursion_div(a,b):
#     if a==0:
#         return 0
#     else:
#         return 1 + recursion_div((a-b),b)
# print(recursion_div(6,2))        

# # print(recursion_div(6,0))# RecursionError: maximum recursion depth exceeded


# list = [1,2,3,4,5]
# print(len(list))

# count  = 0
# for val in list:
#     count = count+1
# print(count)    

# def recursive_power(x,n):
#     if n ==0:
#         return 1
#     else:
#         return x*recursive_power(x,(n-1))

# print(recursive_power(2,5))   

# print(recursive_power(2,-5))   # RecursionError: maximum recursion depth exceeded  
# 



# def recursive_power(x,n):
#     if n<0:
#         return 1
#     else :
#         return x*recursive_power(x,(x-1))
# print(recursive_power(2,-5))    


#! Harshal javadun samajun ghene ha

def dacpower(x,n,res =1):
    if n == 0:
        return 1
    elif n%2== 0:
        res = dacpower(x,n//2)
        return res*res
    else:
        return res*res*x 
print(dacpower(2,2))     


# def odd_no(list2):
#     ans = 0
#     for x in list2:
#         ans = ans^x
#     return ans
# list1 =[3,2,1,1,5,6,9,6,5,2,2,2,9]    
# print(odd_no(list1))


# when ever you perform  the Xor 
# print(2^2^2^2)

# print(6^6^6) #todo -ekade 3 vida 6 aahe tar ha even nahi aahe manun te answer 0 nahi yet 

# print(6^6)  #todo - ekade 2  vida 6 aahe tar ha even aahe  aahe manun te answer 0  yet  aahe 


#find out the lenth of the list with out the use of the len function
# def my_len(list1):
#     count = 0
#     for val in list1:
#         count = count +1
#     return count
# list1 = [2,3,4,5,12,9,-7,17,0]    
# print(my_len(list1))


# find the min and max element with the recursion
# list =[2,3,4,5,12,9,7,17,0]
# max = 17
# min = -7
 
