
# you need to find out the time complexity of these program 

# def fun1(n):# ---
#     if n==0:
#         return 1
#     else:
#         return fun1(n-1)*2
    
# print(fun1(5))    


#?===============================================================================================

# def count(n,d = 1):
#     print(n,end=" ")
#     print(d)
#     d = d+1
#     if n>1:
#         count(n-1)
#         print(d)
# count(3)        

#?===============================================================================================

# def f(n,r = [0]):
#     if n<=0:
#         return 1
#     r[0] = n
#     return f(n-1,r)+r[0]

# s = f(2)
# print(s)

#?===============================================================================================
# finbonicce series 

# a = int(input("Enter a numbeer :"))
# if a&1 ==0:
#     print("Even ")
# else:
#     print("Odd")    
#?===============================================================================================

# def kthbitset(a,k):
#     if  a&(1<<k)==1:
#         return True
#     else:
#         return False
    
# print(kthbitset(8,2))   

#?===============================================================================================
# using bitwise opoeration 
# because of this we dont donvert into  dict and increase the time complexity 
# lst = [2,2, 1,4,4,4,4,5,6,5,6]
# ans = 0
# for i in lst:
#     ans^=i
# print(ans)    

#?===============================================================================================


