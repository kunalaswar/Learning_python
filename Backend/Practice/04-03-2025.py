

# import re
# gd = "bDk6Guc#9LaB7@Qp9&Sz"
# sp = "[abc]"

# result = re.finditer(sp,gd)
# print(result)
# print("*"*50)
# for mat in result:
#     print(f"start Index :{mat.start()},stop Index: {mat.end()}, value :{mat.group()}")
    

# harshal 
#Function to locate the occurrence of the string x in the string s.
# class Solution:
#     def firstOccurence(self,txt,pat):
#         # for i in range(len(txt)):
#         #     if txt[i:i+len(pat)]==pat:
#         #         return i
#         # return -1
#         return txt.find(pat)


    

# s = Solution()
# print(s.firstOccurence("GeeksForGeekssd", "ss"))



# def find(s):
#     for val in s:
#         if val in "aeiou":
#             return True
#         else:
#             return False
# print(find("Harshal") )


 #Function to find the maximum occurring character in a string.

# def getMaxOccurringChar( s ):
#     s1=[]
#     s2 =[]
#     for i in s:
#         if i not in s1:
#             s1.append(i)
#         else:
#             s2.append(i)   
#     print(s1)    
#     print(s2)

# getMaxOccurringChar("output")





# s = "python"
# for val in s:
#     if val =="o":
#         break
#     else:
#         print(val)

# s = "python"
# i = 0
# while(i<len(s)):
#     if s[i]=="o":
#         i = i+1
#         continue
#     else:
#         print(s[i])
#     i = i+1    


# s = "MISSISSIPPI"
# i = 0
# count=0
# while(i<len(s)):
#     if s[i]=="S":
#         count=count+1
#     else:
#         if count==3:
#             break
#         else:
#             print(s[i])    
#     i=i+1    

# s = "MISSISSIPPI"
# i = 0
# count = 0

# while i < len(s):
#     if s[i] == "S":
#         count += 1
#         if count == 3:
#             break  # Stop the loop after 3rd S
#     else:
#         print(s[i])  # Print only non-S characters
#     i += 1



