'''
1 for snake
-1 for water
0 for gun
'''

computer = -1   # Water
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

youDict = {"s": 1, "w": -1, "g": 0}
you = youDict.get(youstr.strip().lower())

if you is None:
    print("Invalid input!")
else:
    if computer == you:
        print("It's a draw!")

    else:
        # Winning logic
        if (computer == -1 and you == 1) or \
           (computer == 1 and you == 0) or \
           (computer == 0 and you == -1):
            print("You win!")
        else:
            print("You lose!")



