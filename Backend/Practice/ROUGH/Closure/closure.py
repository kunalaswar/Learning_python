# def greet():
#     sname = "Rossum"
#     lf = lambda: "Hi "  +sname
#     return lf

# xyz = greet() #Function call    
# print("type xyz",type(xyz))
# res = xyz()
# print(res)

#! ClsEx2.py
def calculate(): #Outer function 
    num =1
    def innerfun(): #Inner function 
        nonlocal num 
        num=num+2
        return num
    return innerfun    


#Main program
inner = calculate()  #Outer function call
# k=inner()
# print(k)
print("----------------OR----------------")
print(inner())
print(inner())
print(inner())