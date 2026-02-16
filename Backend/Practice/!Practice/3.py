# s1={10,20,30}
# s1.add(100)
# s1.add("RS")
# s1.add(True)
# s1.add(2+3j)
# s1.remove(100)
# s1.remove(True)
# print(s1)

#!write a program to swap a number
# a=10
# b=20
# a,b=b,a
# print(a)
# print(b)

#!with out using sort function to sort list

lst=[12,2,9,6,10,18]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)   

# lst=[12,2,9,6,10,18]
# for i in range(len(lst)):
#     print(lst[i])

