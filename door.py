#This file represents a door

door_close = False;
door_open = True;

door = door_open;

can_enter = None;

if door == True:
    can_enter = "You can enter"
else:
    can_enter = "You can't enter!"

print(f"Can enter? \n {can_enter}")