#slot machine program
import random 

def spin_row():
    sym = ['🍒', '🌸', '⭐', '💎', '🔔']
    return [random.choice(sym) for _ in range(3)]
   

def show_row(row):
    print(" | ".join(row))

def get_payroll(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '💎':
            return bet * 10
        elif row[0] == '🌸':
            return bet * 8
        elif row[0] == '🍒':
            return bet * 6
        elif row[0] == '⭐':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 4
    elif row[0] == row[1] :
        if row[0] == '💎':
            return bet * 6
        elif row[0] == '🌸':
            return bet * 5
        elif row[0] == '🍒':
            return bet * 4
        elif row[0] == '⭐':
            return bet * 3
        elif row[0] == '🔔':
            return bet * 2
    return 0
def main():
    bal=100
    print("----------------------------------------------")
    print("Slot Program")
    print("----------------------------------------------")
    print("Symbols: 🍒 🌸 ⭐ 💎 🔔")
    while bal > 0:
        bet = (input("Enter the bet amount: "))
        if not bet.isdigit():
            print("Invalit,use number")
            continue
        bet = int(bet)
        if bet > bal:
            print("Insufficent funds")
            continue
        if bet <= 0:
            print("The bet must be greater than zero")
            continue
        bal -= bet

        row = spin_row()
        print("Spining......")
        show_row(row)
        payroll = get_payroll(row,bet)
        
        if payroll > 0:
            print(f"You won {payroll}")
        else:
            print(f"You lost {bet}")
        bal += payroll
        play_again = input("Do you want to play again(Y/N): ").upper()
        if play_again != 'Y':
            break
main()

        
