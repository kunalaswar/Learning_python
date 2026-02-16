# t1=(10,"kunal",(72,12,56),(78,67,90),"CET")
t1=(10,"kunal",[72,12,56],(78,67,90),"CET")
print(t1,type(t1))
# print(t1[2][0])
# print(t1[3][0])
# print(t1[3])
print(t1[2].sort())
# for val in t1:
#     print(val,type(val),type(t1))



# tup=(10,"kunal",[72,12,56],[78,67,90],"CET")
# print(tup[2])
# print(tup[3])
# tup[2][0]=[1,2,3]
# print(tup[2])
# print(tup ,type(tup))
# print([2])
# print(tup[2][0])
# print(tup[2][0][1])
# print(tup[2][0][0])
# print(tup[2][0][2])
# tup[2][0]=60
# tup[2][1]=600
# print(tup[2])
# tup[-2].sort(reverse=False)
# print(tup)
# # tup[1]="Rossum"# TypeError: 'tuple' object does not support item assignment
# # print(tup)
# # tup[2]=[10,20,30]
# # print[tup] # TypeError: 'tuple' object does not support item assignment
# tup[3][1:3]=[55,66]
# print(tup[3])
# del tup[2][1:3]
# print(tup[2])

# tup=(10, 'kunal', [[1, 2, 3], 12, 56], ("kunal","aniket","harshal"), 'CET')
# k=sorted(tup[-2])
# print(k)
# ['aniket', 'harshal', 'kunal']