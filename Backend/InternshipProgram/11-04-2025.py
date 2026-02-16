
#! 1 to 10 natural number with out loop 

# def print_number(n):
#     if n==0:
#         return
#     else:
            
#         print_number(n-1)
#         print(n)
    
    
# print_number(10)

#! sum of all the natural number with loop 
# def sum_natural(n):
#     if n==0:
#         return 0
#     else:
#         return n + sum_natural(n-1)
# print(sum_natural(10))


#! cheaking  the element is present into the list or not  with out the use of ( in operator)
# def sequential_search(lst,key):
#     i = 0
#     while(len(lst)>i):
#         if lst[i]==key:
#             return True
#         i = i+1
#     return False    

# lst =[-4,55,0,7,1,23,49,11]
# key = int(input("Enter a element which you want to search :"))
# print(sequential_search(lst,key))


#* Using for loop
# def sequencial_search(lst,key):
#     for val in lst:
#         if val ==key:
#             return True
#     return False

# lst =[-4,55,0,7,1,23,49,11]
# key = int(input("Enter a element which you want to search :"))
#print(sequencial_search(lst,key))

#! solve the sequential_search Question using recursive way

# def sequential_search(lst,key):
#     if not lst:
#         return False
#     if lst[0]==key :
#         return True
#     else:
#         return sequential_search(lst[1:],key)
# lst =[-4,55,0,7,1,23,49,11]
# key = int(input("Enter a element which you want to search :"))
# print(sequential_search(lst,key) )        


#! cheaking  the element is present into the list or not  with out the use of ( in operator) and also if exit return its index also 





