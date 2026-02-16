x = ["+91-8446757527","918446757527"," 91-8446757527","+91 8446757527", " 91 8446757527"]
list1 = []
list2 = []
for i in range(len(x)):
    list1.append(int(x[i][len(x[i])-10:]))
    if(x[i][0]=="+"):
        list2.append(x[i][0:3])
    else:
        print("Not an countrycode")
print(list1)
print(list2)