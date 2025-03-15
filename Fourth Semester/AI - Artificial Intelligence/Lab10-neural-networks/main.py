from dolphins import dolphins
from dolphins2 import dolphins2
from football import football
from karate import karate
from karate2 import karate2
from krebs import krebs
from krebs2 import krebs2


def print_menu():
    print("1. Dolphins")
    print("2. Football")
    print("3. Krebs")
    print("4. Karate")
    print("5. Karate 2")
    print("6. Dolphins 2")
    print("7. Krebs 2")
    print("8. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            dolphins()
        elif choice == '2':
            football()
        elif choice == '3':
            krebs()
        elif choice == '4':
            karate()
        elif choice == '5':
            karate2()
        elif choice == '6':
            dolphins2()
        elif choice == '7':
            krebs2()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == '__main__':
    main()
