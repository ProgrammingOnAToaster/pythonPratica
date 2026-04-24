#File that take a name and give up an greeting 

name = str(input("Send a name: "))

time = int(input("What time is it? "))

if(time >= 00 and time < 12):
    print(f"Good Morning,{name} !")

else:
    print(f"Good Afternoon, {name}!")


