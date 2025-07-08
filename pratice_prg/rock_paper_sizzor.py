import random
options= ["rock","paper","sizzor"]
comp = random.choice(options)
print("----------------Rock,Paper,Sizzor game--------------------- ")
name = input("Enter the name of the player: ")
print(f"Player_name: {name}")
print("(Rock,Paper,Sizzor)")
player = input("Enter your Choice: ")
is_playing = True
while is_playing:
    print(f"{name}: {player}")
    print(f"Computer: {comp}")
    if player == comp:
      print("The game is tie....")
    elif player == "rock" and comp == "paper":
      print("The computer wins <3")
    elif player == "rock" and comp == "sizzor":
      print(f"The {name} wins <3")
    elif player == "paper" and comp == "rock":
      print(f"The {name} wins <3")
    elif player == "paper" and comp == "sizzor":
      print("The computer wins <3")
    elif player == "sizzor" and comp == "paper":
      print(f"The {name} wins <3")
    elif player == "sizzor" and comp == "rock":
      print("The computer wins <3")
    else:
      print("invalid")
    break
    