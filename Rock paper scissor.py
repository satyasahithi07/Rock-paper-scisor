import random
print("Press 0 for rock")
print("press 1 for paper")
print("press 2 for scissor")
user_input = int(input("Enter your choice:"))
items=["rock","paper","scissor"]
computer_input = random.randrange(0,2)
print(items[user_input],"selected by user")
print(items[computer_input],"selected by computer")
if user_input==0 and computer_input==1:
    print("computer winner")
elif user_input==1 and computer_input==0:
    print("user winner")
elif user_input==1 and computer_input==2:
    print("computer winner")
elif user_input==2 and computer_input==1:
    print("user winner")
elif user_input==0 and computer_input==2:
     print("user winner")
elif user_input==2 and computer_input==0:
    print("computer winner")
else:
    print("Both are winners")
