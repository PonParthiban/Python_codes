#hangman game
import random
words = ["apple", "mango", "pineapple", "orange"]
hangman_art = {0:("  ",
                  "  ",
                  "  "),
               1:(" O ",
                  "   ",
                  "   "),
               2:(" O ",
                  " | ",
                  "   "),
               3:(" O ",
                  "/| ",
                  "   "),
               4:(" O ",
                  "/|\\",
                  "   "),
               5:(" O ",
                  "/|\\",
                  "/  "),
               6:(" O ",
                  "/|\\ ",
                  "/ \\ "),
              }
def show_man(worng_guesses):
    for l in hangman_art[worng_guesses]:
        print(l)
        
def show_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    worng_guesses = 0
    guesses = set()
    max_att = 6
    #is_running = True
    while  worng_guesses <= max_att:
        show_man(worng_guesses)
        show_hint(hint)
        guess = input("Enter the guess: ")
        
        if len(guess) != 1 or not guess.isalpha():
             print("Invalid Try again!")
             continue
        if guess in guesses:
             print(f"The {guess} is already guessed")
             continue
        guesses.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                 if answer[i]== guess:
                      hint[i] = guess
            continue
        else:
             print("Worng try again")
             worng_guesses+=1
             
        if worng_guesses == max_att:
            show_man(worng_guesses)
            print("\n💀 You've been hanged! Game over.")
            display_answer(answer)
            break
        if "_" not in hint:
             show_man(worng_guesses)
             display_answer(answer)
             print("You Win")
        
        
       
if __name__ == "__main__":
         main()