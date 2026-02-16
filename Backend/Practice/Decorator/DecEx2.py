
def outer(getvals):
    def inner():
        n=getvals
        res=n**2
        return res
    return inner()

def getvals():
    return int(input("Enter a Numerical number :"))
res=outer(getvals())
print("Square is = ",res,type(res))



# def outer(function):
#     def inner():
#         return print("$"*50)
   
#     return inner    
# @outer #! outer(welcome)
# def welcome():
#     print("Hello world ")        
# res=welcome()   
# print(res)


# def box(function):
#     def new_display():
#         # print("*************************")
#         return print("*************************")
#         # print("************************")
#     return new_display
# @box #box(display())
# def display():
#     print("Hello Python")

# res=display()
# print(res)
# # print(type(display))



















