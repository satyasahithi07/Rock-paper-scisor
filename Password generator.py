import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "()[]=°$¥€π√™∆\?{}"
All = lower+upper+numbers+symbols
length = int(input("enter the length of password:\n"))
for i in range(10):
    password="".join(random.sample(All,length))
    print(password )
