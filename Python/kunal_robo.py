import os

# if __init__ =='__main__':
print("Welcome to Robospeaker: ")
while True:
        x=input("Enter what you want me to speak: ")
        if x=="q":
            os.system("say'bye bye' ")
            break
        command=f"say {x}"
        os.system(command)