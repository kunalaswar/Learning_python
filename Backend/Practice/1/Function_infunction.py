# def fun1():
#     print("outer fun")
#     def fun2():
#         print("inner fun")
#     return fun2()    
# res=fun1()
# # print(fun1())
# print(res)
#?=================================================================================================
#! Local variables of outer function become non local variables of inner function.
#! Inner function can access non local variables or local variables of outer function but cannot modify or update directly TO modify OR updates with the help of " nonlocal" keyword

# def outer():
#     def inner():
#         x=100 # Local Variable
#         y=200 # Local Variable
#     inner()
#     print(x)
#     print(y)
       
# outer()
#?=================================================================================================
#! Syntax: nonlocal variable1,variable2,…
# def outer():
#     x=100 # Local Variable
#     y=200 # Local Variable
#     def inner1():
#         print(f"x={x}")
#         print(f"y={y}")
#     def inner2():
#         nonlocal x,y
#         x=800
#         y=900
#     inner1()
#     inner2()
#     inner1()
#     print(f'x={x}')
#     print(f'y={y}')
# outer()

# Output
# x=100
# y=200
# x=800
# y=900
# x=800
# y=900







#?=================================================================================================
























































