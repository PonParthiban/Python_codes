import time

def Starting():
    print("========================================")
    print("🗝️  The Adventure Begins! 🗝️")
    print("========================================")
    print("You are standing at the entrance of an old crypt.")
    time.sleep(1)
    print("It's quiet... too quiet.")
    time.sleep(1)
    print("There are two paths in front of you:")
    time.sleep(1)
    print("[1] A path with flickering torches on the walls.")
    print("[2] A dark passage where you can't see anything.")

def Game_logic():
    choice = input("Enter the choice: ")
    if choice == '1':
        print("You walk down the torch-lit path. The flames flicker as you pass.")
        print("Suddenly, you see a large wooden door with strange symbols on it.")
        print("What do you want to do?")
        print("[a] Open the door ")
        print("[b] Turn back")
        path1_choice = input("Enter the choice(a/b): ")
        if path1_choice == 'a':
            print("You slowly push the door open...")
            print("Inside, you find a glowing treasure chest filled with gold and ancient gems!")
            print("✨ Congratulations! You found the treasure and survived the crypt! ✨")
        else:
            print("You turn around, but the path is gone!")
            print("The torches go out one by one... and darkness swallows you whole.")
            print("☠️ You are never seen again. Game Over. ☠️")
    elif choice == '2':
        print("You step into the darkness. You can't see anything.")
        print("You hear something moving ahead...")
        print("What do you want to do?")
        print("[a] Light a match  ")
        print("[b] Keep walking in the dark")
        path1_choice = input("Enter the choice(a/b): ")
        if path1_choice == 'a':
            print("You strike a match. A ghostly figure appears in front of you!")
            print("But instead of attacking, it gently points toward a secret exit.")
            print("✨ You follow it and escape safely. You're free! ✨")
        else:
            print("You walk forward, hoping for the best...")
            print("Suddenly, the ground disappears beneath you.")
            print("🕳️ You fall into a deep pit. No one hears your screams. Game Over. 🕳️")
    else:
        print("Invalid Choice")

def main():
   is_running = "yes"
   while is_running == 'yes': 
    Starting()
    Game_logic()
    is_running = input("Do you want to play again?(yes/no): ").islower()
if __name__ == "__main__":
    main()













    



