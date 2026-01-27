name= input("Enter your name:")
print("Welcome", name , "to this adventure!")

answer = input("You are on a dirt road,It has come to an end you can go left or right. Which way would you like to go???")

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross ")
    
    if answer == 'swim':
        print('You swam across and were eaten by an aligator')
    elif answer=='walk':
        print('You walked and were eaten byy tiger')
    else:
        print('not a valid option.You lose')


elif answer == "right":
    answer = input ("You come to a bridge, it looks woobly, Do you want to cross it or head back?(cross/back)")
    if answer == 'back':
        print('You go back and loose.')
    elif answer=='cross':
        answer= input("You cross the bridge and meet a stranger.Do you talk to them(yes/no)?")
        if answer =="yes":
            print("You talk to stranger and they gave u gold bar,You won")
        elif answer=="no":
            print("You ignore the stranger and they got offended and you lose ")
        else:
            print('Not a valid option.You lose')
    else:
        print('not a valid option.You lose')
    
else:
    print('Not a valid option. You lose')
    
print('Thank u for playing', name)