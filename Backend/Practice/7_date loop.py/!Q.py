
# #! harshal enumerate() function
# l1 = [25000,30000,22000,40000,100000]

# for i,j in enumerate(l1,start=2020):
#     print(f"Year : {i} Revenue : {j}")



#! WRITE A PROGRAM TO FIND THE PRODUCT OF A GIVEN NUMBER :
# n = int(input("enter a number  : "))
# p= 1
# while(n>0):
#      r = n % 10 
#      p = p*r
#      n = n//10
# print(p)
#! WRITE A PROGRAM TO FIND THE PRODUCT OF A GIVEN NUMBER :
# n=int(input("Enter a number :"))

# for i in range(1,n+1):
#     r=n%10
#     p=p*r















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