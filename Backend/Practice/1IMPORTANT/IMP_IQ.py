
#^------------------------------------------------------------------------------------------------------
# dict1={}
# def find_max_length_word(list1):
#     dict1 = {i:len(i) for i in list1}
#     max = 0
#     # print(dict1)
#     for i in dict1:
#         # print(dict1[i])
#         if dict1[i]>max:
#             max=dict1[i]
#             idx=i
            
#     return idx,max

# list1 = [input("Enter names :") for i in range(1,5)]
# word,l=find_max_length_word(list1)
# print(word,l)

#^--------------------------------------------------------------------------------------------------
# lst=[1,2,33,33,33,33,33,33,5,6,7,1,4,6]

# for val in lst:
#     if val==33:
#         continue
#     lst.append(val)
# print(lst)
# i=0
# while(i<=len(lst)-1):
#     # print(lst[i])
#     if lst[i]<33:
#         lst.append(lst[i])
#     i=i+1




#^--------------------------------------------------------------------------------------------------
# l1=[1,2,10,10,10,10,5,10,10,10,10,3,4,4]
# # d1={ val:l1.count(val) for val in l1  }
# # print(d1)
# d1={}
# for val in l1:
#     d1[val]=l1.count(val)
# print(d1)    


#^------------------------------------------------------------------------------------------------------

# lst=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# l1 = [0,1,2,3,4,]
# l1 = []
# for i in range(len(lst)):
#     if len(l1)==0:
#         l1.append(lst[i])
#     elif(l1[-1]==lst[i]):pass    
#     else:
#         l1.append(lst[i])
# print(l1)    

#!Fibonacci series
#^---------------------------------------------------------------------------------------------------
# n=int(input('Enter a number for upto you want:'))
# a=0
# b=1
# for val in range(1,n+1):
#     c=a+b
#     a=b
#     b=c
#     print(c)

#^---------------------------------------------------------------------------------------------------



# lst = [2,32,312,312,4,4,34,32,3,4]
# lst.sort()
# print("Maximum :",lst[-1])
# print("Second Maximum :",(lst[-lst.count(lst[-1])-1]))



#User function Template for python3
# class Solution:
#     def revStr (self, s : str) -> str :
#         # code here 
#         lst=[]
#         return s[::-1]
        
           
        
# s = Solution()        
# print(s.revStr("GeeksforGeeks"))



# class Solution:
    
#     #Function to find the maximum occurring character in a string.
#     def getMaxOccurringChar(self, s):
#         #code here
#         count=0
#         wordlen = dict()
#         for j in s:
#             if j not in s:
#                 wordlen[j]=len(j)
#             else:
#                 wordlen[j]=len(j)+1
#         return wordlen    

    
# s = Solution()            
# print(s.getMaxOccurringChar("output"))

            
# class Solution:
#     def convert(self, s):
#         # code here:
#         return s.title()
    
# s = Solution()   
# print(s.convert("i love programming"))



#===================================================================================================
# def longestValidParentheses(s):
#     stack = [-1]  # Initial marker to handle edge cases
#     max_length = 0

#     for i, char in enumerate(s):
#         if char == "(":
#             stack.append(i)  # Store index of '('
#         else:
#             stack.pop()  # Remove last '('
#             if stack:
#                 max_length = max(max_length, i - stack[-1])  # Calculate length
#             else:
#                 stack.append(i)  # Store invalid ')' index

#     return max_length

# # Test cases
# print(longestValidParentheses("(()("))      # Output: 2
# print(longestValidParentheses("()(())("))   # Output: 6


# class Solution:
#     def sort1(self, s): 
#         # Convert string to list and sort it in reverse order
#         lst = sorted(list(s))
#         return "".join(lst)  # Convert back to string
        
# s = Solution()        
# print(s.sort1("edcab"))  # Output: "edcba"


# class Solution:
#     # Function to find uncommon characters between two strings.
#     def uncommonChars(self, s1, s2):
#         #code here
#         set1 = set(s1)
#         set2 = set(s2)
#         uncommon_value = (set1^set2)
#         return "".join(sorted(uncommon_value))
    
                    
# s1 = "geeksforgeeks"
# s2 = "geeksquiz"        
# s = Solution()    
# print(s.uncommonChars(s1,s2))




# class Solution:
#     def convert(self, s):
#         # code here
#         return s.title()
# s = Solution()
# print(s.convert( "i love programming"))


#^---------------------------------------------------------------------------------------------------
#* harshal 

# num= 123,56
# sum of digits = 6

# def count_sum(n):
#     res = 0
#     i = 0
#     while(n>0):
#         d = n % 10
#         res = res + d
#         n  = n//10
#     return res
# s = count_sum(123)        
# print("sum : ",s)


# def first_sum(n):
#     res = 0
#     while(n>0):
#         d = n % 10
#         res = res + d
#         n = n//10
#     return second_sum(res)
# def  second_sum(res)  :
#     res2 = 0 
#     while(res>0):
#         d2 = res % 10
#         res2 = res2 + d2
#         res = res//10  
#     return res2 
       

# s = first_sum(64)
# # s2 = second_sum(s)
# print("second sum :",s)


# def first_sum(n):
#     while True:
#         res = 0
#         while(n>0):
#             d = n % 10
#             res = res + d
#             n = n//10
#         if res>9:
#             n=res
#         else:break
#     return res

# print("Sum :",first_sum(56))


