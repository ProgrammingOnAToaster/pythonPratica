#File that take a name and give up an greeting 
name = str(input("Send a name: "))

time = int(input("What time is it? "))

if(time >= 00 and time < 12):
    print("Good Morning, " + name + "!")

else:
    print("Good Afternoon, " + name + "!")


