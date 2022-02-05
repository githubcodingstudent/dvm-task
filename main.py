import csv
import os


def register():
    while True:
        ac = input('Account number:')
        with open('database.csv', 'r', newline='') as db:
            rd = csv.reader(db)
            existing = []
            while True:
                try:

                    existing.append(next(rd)[0])
                except StopIteration:
                    break
            if ac in existing:
                print('Account already exists. Try again')
            else:
                break

    while True:
        pin = input('Pin: ')
        if not len(pin) == 4:
            print('Pin length incorrect')
        elif not pin.isnumeric():
            print('Please enter a numeric PIN.')
        elif pin == input('Verify Pin: '):
            break
        else:
            print('Pins do not Match enter again.')

    with open('database.csv', 'a', newline='') as db:
        db_wtr = csv.writer(db)
        db_wtr.writerow([ac, pin, 0])
        db.close()

    print('Successfully registered')


def access():
    ac = input("Enter your account number: ")
    pin = input("Enter your pin: ")
    with open('database.csv', 'r', newline='') as db:
        rd = csv.reader(db)
        for i in rd:
            if i[0] == ac:
                if i[1] == pin:
                    balance = int(i[2])
                else:
                    print('Incorrect PIN')
                    return
                break
        else:
            print('Account not found.')
            return

    choice = 0
    while choice != 4:
        print("\n\n**** Menu *****")
        print("1 == balance")
        print("2 == deposit")
        print("3 == withdraw")
        print("4 == cancel\n")

        choice = int(input("\nEnter your option:\n"))
        if choice == 1:
            print("Balance = ", balance)
        elif choice == 2:
            dep = int(input("Enter your deposit: "))
            balance += dep
            print("Deposited amount: ", dep)
            print("Balance = ", balance)
        elif choice == 3:
            wit = int(input("Enter the amount to withdraw: "))
            if balance < wit:
                print("Insufficient Balance.")
                continue
            balance -= wit
            print("Withdrawn amount: ", wit)
            print("Balance = ", balance)
        elif choice == 4:
            with open('database.csv', 'r', newline='') as db, open('temp.csv', 'w', newline='') as new:
                rd = csv.reader(db)
                wt = csv.writer(new)
                for i in rd:
                    if i[0] == ac:
                        i[2] = str(balance)
                    wt.writerow(i)
                db.close()
                new.close()
            os.remove('database.csv')
            os.rename('temp.csv', 'database.csv')
            print('Session ended,goodbye.')
        else:
            print("Invalid Entry")


def home():
    option = input("Login | Signup: ")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please choose an option")


if __name__ == '__main__':
    while True:
        home()
