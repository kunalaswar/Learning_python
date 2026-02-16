
import sys
print(sys.argv)
a = int(sys.argv[1])
b = int(sys.argv[2])
c = sys.argv[3]
match(c):
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*' :
        print(a*b)
    case '/':
        print(a/b)
