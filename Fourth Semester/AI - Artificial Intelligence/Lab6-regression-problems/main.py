import problema1
import problema1b
import problema2
import problema2b
import problema3
import problema3b


def print_menu():
    print("1. Run problem 1")
    print("2. Run problem 1b")
    print("3. Run problem 2")
    print("4. Run problem 2b")
    print("5. Run problem 3")
    print("6. Run problem 3b")
    print("7. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            problema1.p1()
        elif choice == '2':
            problema1b.p1b()
        elif choice == '3':
            problema2.p2()
        elif choice == '4':
            problema2b.p2()
        elif choice == '5':
            problema3.p3()
        elif choice == '6':
            problema3b.p3b()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == '__main__':
    main()
