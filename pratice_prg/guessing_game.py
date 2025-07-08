import random
low_num = int(input("Enter the lowest number for the game: "))
high_num = int(input("Enter the highest number for the game: "))
answer = random.randint(low_num, high_num)
guesses = 0
is_guessing = True
while is_guessing:
 guess = int(input(f"Enter the number between {low_num} and {high_num}: "))
 guesses+= 1
 if guess < low_num and guess > high_num:
    print("Invalid,try again!")
 elif guess < answer:
    print("Too small,try again!")
 elif guess > answer:
    print("Too large,try again!")
 else:
    print(f"The correct answer is {answer} ")
    print(f"Total number of guesses {guesses} ")
    is_guessing = False

    
  