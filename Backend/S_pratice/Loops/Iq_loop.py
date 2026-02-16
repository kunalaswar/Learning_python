
#! WRITE A PROGRAM TO FIND THE PRODUCT OF A GIVEN NUMBER :
# n = int(input("enter a number  : "))
# p= 1
# while(n>0):
#      r = n % 10 
#      p = p*r
#      n = n//10
# print(p)
# ? =========================================================================================================
#! WRITE A PROGRAM FOR FINDING A EVEN AND ODD VALUES OF GIVEN NUMBER 
# n = int(input("enter a number  : "))
# even_values=[]
# odd_values= set()
# while(n>0):
#      r = n % 10 
#      if r%2 ==0:
#       even_values.append(r)
#      else:
#       odd_values.add(r)
#      n = n//10
# print(even_values)
# print(odd_values)
# ? =========================================================================================================
#! SUM OF EVEN NUMBER OF GIVEN VALUE 
# n = int(input("enter a number  : "))
# s  = 0
# while(n>0):
#      r = n % 10 
#      if r%2 ==0: 
#           s = s+r
#      n = n//10
# print(s)
# ? =========================================================================================================
#! SUM OF ODD NUMBER OF GIVEN VALUE 
# n = int(input("enter a number  : "))
# s  = 0
# while(n>0):
#      r = n % 10 
#      if r%2 !=0: 
#           print(r)
#           s = s+r
#      n = n//10
# print(f"sum of odd number is {s}")

# ? =========================================================================================================
#! SUM OF EVEN NUMBER AND ODD NUMBER OF GIVEN VALUE 
# n = int(input("enter a number  : "))
# even_number  = 0
# odd_number = 0
# while(n>0):
#      r = n % 10 
#      if r%2 ==0: 
#      #  print("EVEN NUMBER :",r)
#       even_number= even_number+r
#      else:
#      #    print("ODD NUMBER : ",r)
#         odd_number=odd_number+r
          
#      n = n//10
# print(even_number)
# print(odd_number)
# ? =========================================================================================================
#! SUM OF EVEN NUMBER AND PRODUCT OF GIVEN VALUE
# n = int(input("enter a number  : "))
# sum_even_number = 0
# product_odd_number = 1
# while n > 0:
#     r = n % 10
#     if r % 2 == 0:
#         sum_even_number = sum_even_number + r
#     else:
#         product_odd_number = product_odd_number * r

#     n = n // 10
# print(sum_even_number)
# print(product_odd_number)
# ? =========================================================================================================
#! PROGRAM FOR FINDING SUM OF SQUARES OF GIVEN NUMBER 
# num = int(input("ENTER A NUMBER : "))
# Tnum = num
# sum_squares= 0
# while(num>0):
#      r = num%10
#      sum_squares = sum_squares+ r*r  #or r**2
#      num = num//10
# print(f"sum of {Tnum} = {sum_squares}")
# ? =========================================================================================================
#! PROGRAM FOR FINDING SUM OF CUBE OF GIVEN NUMBER 
# num = int(input("ENTER A NUMBER : "))
# Tnum = num
# sum_cubes= 0
# while(num>0):
#      r = num%10
#      sum_cubes = sum_cubes+ r**3 #or r*r*r
#      num = num//10
# print(f"sum of {Tnum} = {sum_cubes}")
# ? =========================================================================================================
#! PROGRAM FOR CHECKING WHETHER GIVEN NUMBER IS PALINDROM OR NOT
# num = int(input("ENTER A NUMBER : "))
# O_num = num
# reversed_number = 0
# while(num>0):
#      r = num%10
#      reversed_number= reversed_number*10+r
#      num = num//10

# if reversed_number == O_num:
#  print(f"{O_num} is palindrom")
# else:
#  print(f"{O_num} is not a palindrom")

# ? =========================================================================================================
#! FINDING THE FACTORS OF GIVEN NUMBER 
# num = int(input("enter a value : "))
# Tnum = num
# fact = 1
# while(num>0):
#      r = num%10
#      fact = fact*r
#      num = num//10
# print(f"factorial of {Tnum} is {fact}")

# ? =========================================================================================================
#! WRITE A PROGRAM TO FIND LENGTH (COUNT) OF GIVEN NUMBER
# n = int(input("ENTER A NUMBER : "))
# on = n
# count = 0
# while(n>0):
#      n = n//10
#      count = count+1

# print(f"THE LENGTH OR COUNT OF {on} is {count}")
# ? =========================================================================================================
# #! WRITE A PROGRAM TO FIND THE PRODUCT OF A GIVEN NUMBER :
# num=int(input("Enter a number :"))
# p=1
# while(num>0):
#     res=num%10
#     p=p*num
#     num=num//10
# print(p)


# #! WRITE A PROGRAM FOR FINDING A EVEN AND ODD VALUES OF GIVEN NUMBER 
# num=int (input("Enter a number:"))

# for i in range(1,num):
#     res=i%10
#     if(res%2==0):
#         print(f"EVEN number {res}")
#     else:
#        print(f"EVEN number {res}")
#     num=num//10      


# num=int(input("Enter a number :"))
# lst1=[]
# lst2=[]
# while(num>0):
#     res=num%10
#     if(res%2==0):
#         print(f"EVEN number {res}")
#         lst1.append(res)
#     else:
#        print(f"EVEN number {res}")
#        lst2.append(res)
#     num=num//10   
# print(lst1)
# print(lst2)

# #! SUM OF EVEN NUMBER OF GIVEN VALUE 

# num=int(input("Enter a number:"))
# sum=0
# lst=[]
# while(num>0):
#     res=num%10
#     if(res%2==0):
#         sum=sum+res
#         lst.append(res)
#     num=num//10
# print(lst)    
# print(sum)        

# #! SUM OF ODD NUMBER OF GIVEN VALUE 
# num=int(input("Enter a number:"))
# sum=0
# lst=[]
# while(num>0):
#     res=num%10
#     if(res%2!=0):
#         print(res,end=" ")
#         sum=sum+res
#         print()
#         lst.append(res)
#         lst.reverse()
#     num=num//10
# print(lst)        
# print(sum)

# #! SUM OF EVEN NUMBER AND ODD NUMBER OF GIVEN VALUE 

# num=int(input("Enter a number:"))
# even_sum=0
# odd_sum=0
# lst1=[]
# lst2=[]
# while(num>0):
#     res=num%10
#     if(res%2==0):
#         even_sum=even_sum+res
#         print(res)
#         lst1.append(res)
#     else:
#         odd_sum=odd_sum+res    
#         print(res)
#         lst2.append(res)
#     num=num//10
# print(f" sum Even number{lst1} is {even_sum} ")    
# print(f" sum Even number{lst2} is {odd_sum} ")    
# print(lst2)    
# print(even_sum,odd_sum)        

# ! SUM OF EVEN NUMBER AND PRODUCT OF GIVEN VALUE
# num=int(input("Enter a number :"))
# even_sum=0
# product=1
# while(num>0):
#     res=num%10
#     product=product*res
#     if(res%2==0):
#         print(f"even number {res}")
#     num=num//10
# print(product)        
## print(even_sum)        
        
# #! PROGRAM FOR CHECKING WHETHER GIVEN NUMBER IS PALINDROM OR NOT
# num=input("Enter a number :")
# while(int(num)>0):
#     res=int(num)%10
#     if(str(res)==str(res)[::-1]):
#         print( f"{res} this value is palindrome ",end=" ")
#     else:
#         print(f" {res} value is not palindrome")    
#     num=int(num)//10

# #! FINDING THE FACTORS OF GIVEN NUMBER 
# num=int(input("Enter a number:"))
# fact=1
# while(num>0):
#     res=num%10
#     fact=fact*res
#     num=num//10
# print(fact)    










# #! WRITE A PROGRAM TO FIND LENGTH (COUNT) OF GIVEN NUMBER

# num=int(input("Enter a number:"))
# count=0
# while(num>0):
#     res=num%10
#     count=count+1
#     num=num//10
# print(count)    

#! WRITE A PROGRAM TO FIND THE PRODUCT OF A GIVEN NUMBER :
# num=int(input("Enter a number :"))
# pro=1
# while(num>0):
#      r = num%10
#      pro=pro*num
#      num=num//10
# print(pro)
#! PROGRAM FOR CHECKING WHETHER GIVEN NUMBER IS PALINDROM OR NOT

# st=input("Enter a value :")
# i=0
# while(i<len(st)):
#      print(st[i])
#      i=i+1
# st=input("Enter a number:")
# i=0
# while(i<len(st)):
#      if(st[i]==st[i][::-1]):
#           print("it is palindeome")
#           i=i+1
# st=input("Enter a value :")
# if(st==st[::-1]):
#     print("it is palindeome") 
# else:
#      print(" not palindeome")

# st=int(input("Enter a value :"))
# if(str(st)==str(st)[::-1]):
#     print("it is palindeome") 
# else:
#      print(" not palindeome")

#! PROGRAM FOR CHECKING WHETHER GIVEN NUMBER IS PALINDROM OR NOT
# num=int(input("Enter a number :"))
# s=" "
# while(num>0):
#      res=num%10
#      if(str(num)==str(res)[::-1]):
#           print('palindeome')
#      else:
#            print(" it is not palindeome")      
#      num=num//10







