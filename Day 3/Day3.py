print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
print("You see the road split into two.")
lr = input("Where would you like to go? (left/right)-")
if lr.lower()=="left":
    print("You took the left road. You continue walking and finally come across a river.")
    sw = input("Would you like to swim or wait? ")
    if sw.lower()=="wait":
        print("You decided to wait. After 10 minutes, three doors magically appear on your right.")
        rby = input("Which door would you like to go? (blue/yellow/red)-")
        if rby.lower()=="yellow":
            print("You found the treasure!")
        elif rby.lower()=="red":
            print("You stepped in and fell off a 12 storey building. Game over!")
        else:
            print("You entered a room full of bears. Game over!")
    else:
        print("The rivers was filled with crocodiles. Game over!")
else:
    print("You keep on walking. 10 days..... 20 days...... no end..... Game over!")