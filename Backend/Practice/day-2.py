

#* ternary conditions 
# age = 18
# res = True if age >= 18 else False
# print(res)

# name = input("Enter a Name :")
# count = 0
# for _ in name:
#     count = count+1
# print(count)

# for i in [1,2,3]:
#     print("python")


#* program of uppercase with out using uppercase function 

# def uppercase():
#     str1 = input("Enter a Text :")
#     str2 = ""
#     for ch in str1:
#         if ch>="a" and ch <="z":
#             str2 = str2 + chr(ord(ch)-32)
#         else:
#             str2 = str2 + ch
#     print("Normal strings =",str1)            
#     print("uppercase strings =",str2)            

# uppercase()  

# def Lowercase():
#     str1 = input("Enter a Text :")
#     str2 = ""
#     for ch in str1:
#         if ch>="A" and ch <="Z":
#             str2 = str2 + chr(ord(ch)+32)
#         else:
#             str2 = str2 + ch
#     print("Normal strings =",str1)            
#     print("Lowercase strings =",str2)            

# Lowercase() 


#* program for finding the factorial of 1 to 10 

# for num in range(1,10):
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact *i
#     print(f"the factrial of {num} = {fact}")

#* max min function without using predefined function 
# lst1 = [10,50,20,40,30,70,60,80,90]
# maxvalue = 0
# for val in lst1:
#     if maxvalue < val:
#         maxvalue= val
# print(f"maximum value is = ",maxvalue)        

# lst1 = [50,20,10,40,30,70,60,80,90]
# minvalue = lst1[0]
# for val in lst1:
#     if minvalue >= val:
#         minvalue = val 
# print(f"minimum value is = ",minvalue)        

 
# lst = [1,2,3,4,5,6,7,8,9]
# lst[len(lst):] = [10]
# print(lst)

# lst = [1,2,3,4,5,6]
# lst = lst+[10]
# print(lst)

# lst = [1,2,3,4,5,6]
# lst[len(lst):len(lst)] = [11,12,13]
# print(lst)

#* WAP to sort the Element into of list in ascending order 

# n  = int(input("Enter How many element :"))
# lst = []
# for i in range(1,n+1):
#     value = int(input(f"Enter number {i} = "))
#     lst.append(value)
# # print(lst)    

# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if lst[i]<lst[j]:
#             lst[i],lst[j] = lst[j],lst[i]
# print(lst)

#* without using insert method 

# lst = [1,2,3,4,5]
# lst[1:1] = [20]  #todo - insert method without using predefined method using this 
# print(lst)
# lst[:4] = [77]
# print(lst)



# lst = [5,15,10,25]
# # lst.sort()
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         print(lst[i],lst[j])
#         print("---------")

#         if lst[i]<lst[j]:
#             lst[i],lst[j] = lst[j],lst[i]
# print(lst)

# fmaxc = lst.count(max(lst))
# fminc = lst.count(min(lst))
# print(f"second max = {lst[fmaxc]}")
# print(f"second min = {lst[fminc]}")



# lst1 = []
# for num in range(1,11):
#     lst1.append(num**2)
# print(lst1)  

# lst= [num**2 for num in range(1,11)]
# print(lst)

# lst=[[num for num in range(2) ] for i in range(2)]
# print(lst)

#* fibonacii series

# n1 = 0
# n2 = 1
# n3 = 0
# print(n1,n2,end = " ")
# while(n3<53):
#     n3 = n1+n2
#     n1 = n2
#     n2 = n3
#     print(n3,end =" ")    

#* program for checking at least one alphabets and one digits

# str1 = input("Enter a string :")
# alphac,digitc = 0,0
# for ch in str1:
#     if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
#         alphac = alphac + 1
#     elif "0 "<= ch <='9':
#         digitc = digitc + 1
# print(alphac,digitc)
# if alphac > 0 and digitc > 0:
#     print(f'{str1} contain both the alphabets and digits ')     
# else:
#     print(f'{str1} Not contain the alphabets and digits ')     

# str1 = input("Enter a number :")
# for ch in str1:
#     c = str1.count(ch)
#     print(f'{ch} --->{c}') 


#* maximum frequecy character into the string 

# str1 = input("Enter a string : ") #aaaabcd
# m = 0
# ch =""
# for i in str1:
#     c = str1.count(i)
#     # print(i,c)
#     if c > m :
#         m=c
#         ch = i
# print(f'{ch} ---> {m}')        


# 
# l1 = [10,20,30]
# l2 = ["rs","ts","es",["1","2","3"]]
# l1.extend(l2)
# print(l1)

# print(l1[6])

# tup = (10,20,30)
# print(tup[0])

# lst = ["python",]
# print(lst)

# tup = ("python",)
# print(tup)

# lst  = [50,30,70,80,20,10]
# lst.sort()
# print(sorted(lst)) #* sorted() is a built-in function



