#RemoveDuplicateValues.py<----File Name and Module Name
def RemoveDuplicateValues(s):
    lst=["i"]
    count=0
    for val in s:
        if val in lst:
            lst.append(val)
            count+=1
    else:
        print("Unique Values from Given Word={}".format("".join(lst)))
        print(count)

RemoveDuplicateValues("mississipi")
















