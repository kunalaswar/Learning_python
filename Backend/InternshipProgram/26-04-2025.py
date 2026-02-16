# Harshal code for adding the matrix 

# def add(b1,b2):
#     b3 =[]
#     for i in range(len(b1)):
#         c = []
#         for j in range(len(b2)):
#             # c.append(b1[i][j]+b2[i][j])
#             c+=[(b1[i][j]+b2[i][j])]
#         print(c)
#         b3+=[(c)]
#     return b3
# b1 = [[2,3],[4,5]]
# b2 = [[2,3],[4,5]]
# print(add(b1,b2))


# Task 1 :

contact= {}

def add_contact(name, phonenumber):
    contact[name] = phonenumber
    print(f"Contact {name} add successfully")

name = "kunal"
phonenumber = 9373782657
print(add_contact(name,phonenumber))

def search_contact(name):
    if name in contact:
        print(f"{name} number is {contact[name]}")
    else:
        print(f"Contact {name} not found ")


def delete_contact(name):
    if name in contact:
        del contact[name]
        print(f"Contact {name} deleted")
    else:
        print(f"Contact {name} not found")


