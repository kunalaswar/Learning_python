try:
    s1=input("Enter a number :")
    s2=input("Enter a number :")
    a=int(s1)
    b=int(s2)
    c=a/b
    s="python"
    print(s[1])

except (ValueError,ZeroDivisionError):
    print("Dont enter a almun special symbol or pure str")    
    print("Dont Enter a zero for DEN...") 
# except IndexError:
#     print("you not provide proper index ")
except:
    print("Oooop some thing Went wrong Check U code properly ")       
else:
    print("Div = ",c)

finally:
    print("-------------finally--------------------")
