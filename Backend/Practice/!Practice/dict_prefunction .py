# clear functioin in Dict
# d1={"python":1,"c":2,"c++":3,"java":4}
# print(d1,type(d1))
# d1.clear()
# print(d1,type(d1))
# d1.clear()
# print(d1,type(d1))
# d1.clear()
# print(d1,type(d1))

# print(d1.clear())


#pop function in dict

# d1={10:1.1,20:2.2,30:3.3,40:4.4}
# print(d1)
# d1.pop(10)
# print(d1)
# print(d1.pop(200))

# {}.pop(10)
# print(set())#KeyError: 10
# print(dict().pop(100)) #KeyError: 100

# popitem() in dict function
# d1={10:1.1,20:2.2,30:3.3,40:4.4}
# print(d1)
# print(d1.popitem(),id(d1))
# print(d1.popitem(),id(d1))
# print(d1.popitem(),id(d1))
# print(d1.popitem(),id(d1))

#dict keys in dict function
# d1={"python":1,"c":2,"c++":3,"java":4}
# print(d1,type(d1))
# ks=d1.keys()
# print(ks,type(ks))
# for k in ks:
    # print(k)
# for k in d1.keys():
#     print(k)

 
# vs=d1.values()
# print(vs,type(vs))




#items in dict function
# d2={"python":1,"c":2,"c++":3,"java":4}
# print(d2,type(d2))
# kvs=d2.items()
# print(kvs,type(kvs)) #dict_items([('python', 1), ('c', 2), ('c++', 3), ('java', 4)]) 

# for kv in d2.items():
#     print(kv)

# for k,v in d2.items():
#     print(k,"--->",v)






#  RULE-1) Dict in Dict  7 Rules

# d2={"python":10,"c":20,"c++":30,"java":40}
# print(d2,type(d2))
# # for  k in d2.keys():
# #     print(k)

# # for  v in d2.values():
# #     print(v)

# print(d2.items())    
# for k in d2.items():
#     print(k)

# for k,v in d2.items():
#     # print("cls
#     #  Both print key,value using items()",k,v)
#     print(" Both print key,value using items()",k,v)


# d2={"python":10,"c":20,"c++":30,"java":40}
# # print(d2,type(d2))
# for k,v in d2.items():
#     print(k,"--->",v,"--->",type(k),"--->",type(d2))

# d3={"sno":10,"name":"rs","IM":{"c":16,"os":14,"c++":18}}    
# print(d3,type(d3))
# print(d3.get("sno"))
# print(d3.pop("name"))
# print(d3.pop("sno"))
# print(d3,type(d3))

# for val in d3:
    # print(val,d3[values]) #Error

# for k,v in d3["IM"].items():
#     print(k,"--->",v)    

# print(d3["IM"])
# print(d3["IM"]["c"])
# d3["IM"]["c"]=100 #updating the dict {'c': 100, 'os': 14, 'c++': 18}
# print(d3["IM"])

# d3["IM"].get("os")=100
# print(d3) #SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?

#TO add the new dictnoary in the dict
# d3["EM"]={"DBMS":90,"NW":60,"DSA":80}
# print(d3,type(d3))
# #To pop the value in the dict
# d3["EM"].pop("NW")
# print(d3,type(d3))
# #To clear the dict in the dict
# d3["EM"].clear()
# print(d3,type(d3))
# #To popitem in the dict to remove an End item in the dict
# d3.popitem()
# print(d3,type(d3))
# d3.popitem()
# print(d3,type(d3))

# d3={"sno":10,"name":"rs","IM":{"c":16,"os":14,"c++":18}}    
# print(d3,type(d3))
# # To add the total dict value in the dict
# d3["TotalIM"]=d3["IM"]["c"]+d3["IM"]["os"]+d3["IM"]["c++"]
# print(d3["TotalIM"])
# print(d3,type(d3))


#  RULE-2) list in Dict  8 Rules

# d1={"sno":10,"name":"rs","IM":[18,12,19],"EM":[56,67,80]}    
# print(d1,type(d1))
# for val in d1["IM"]:
#     print(val) 
# d1["IM"].remove(18)
# print(d1["IM"])
# print(d1)
# # d1["IM"].values()
# # print(d1)     #  AttributeError: 'list' object has no attribute 'values'
# print(sum(d1.get("EM"))) # 203
# # d1["TotalIMEM"]=d1["EM"]+d1["IM"]
# d1["TotalIMEM"]=sum(d1["EM"])+sum(d1["IM"])
# print(d1["TotalIMEM"]) # 230

# d1["EM"].append(15)
# print(d1["EM"]) # [56, 67, 80, 15]

# d1["IM"].insert(1,99)
# print(d1["IM"]) # [18, 99, 12, 19]







#  RULE-3) tuple in Dict  8 Rules

# d1={"sno":10,"name":"rs","IM":(18,12,19),"EM":(56,67,80)}    
# print(d1,type(d1))
# print(d1["EM"].values()) # AttributeError: 'tuple' object has no attribute 'values'
# for k,v in d1.items():
#     print(k,"--->",v,"--->",type(k),"--->",type(v),"--->",type(d1))
    # {'sno': 10, 'name': 'rs', 'IM': (18, 12, 19), 'EM': (56, 67, 80)} <class 'dict'>
    # sno ---> 10 ---> <class 'str'> ---> <class 'int'> ---> <class 'dict'> 
    # name ---> rs ---> <class 'str'> ---> <class 'str'> ---> <class 'dict'>
    # IM ---> (18, 12, 19) ---> <class 'str'> ---> <class 'tuple'> ---> <class 'dict'>
    # EM ---> (56, 67, 80) ---> <class 'str'> ---> <class 'tuple'> ---> <class 'dict'>

# d1.pop("EM")    #To pop the perticular value in dict pop() method 
# print(d1,type(d1))
# d1["EM"]=(4,1,3,2)
# print(d1,type(d1))
# print(sorted(d1["EM"]))    # [1, 2, 3, 4]
# print(tuple(sorted(d1["EM"]))) #(1, 2, 3, 4)


#RULE- 7) dict in list  7 Rules
# lst=[10,"RS",{"c":18,"c++":19,"os":20}]  
# for val in lst:
#     print(val,"--->",type(val),"--->",type(lst))

# print(lst[2].values()) #dict_values([18, 19, 20])
# print(lst[2])  #  {'c': 18, 'c++': 19, 'os': 20}
# lst[-1]["PYM"]=18
# print(lst,type(lst))
# lst.append({"A":10,"B":20})
# print(lst,type(lst))


# 12) RULE dict in tuple
# tpl=(10,"RS",{"C":18,"c++":16,"OS":20},"JNTU")
# print(tpl,type(tpl))
# for val in tpl:
#     print(val,"--->",type(val),"--->",type(tpl))


# RULE dict in set #NOT POSSIBLE
#s1={10,"RS",{"C":18,"C++":19,"OS":20}}
# print(s1)  TypeError: unhashable type: 'dict'
# print({}.clear())





