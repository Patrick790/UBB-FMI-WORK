import bleu
import p1a
import p1b
import p2a
import p2c
import bleu


def print_menu():
    print("1. Run problem 1a")
    print("2. Run problem 1b")
    print("3. Run problem 2a+b")
    print("4. Run problem 2e")
    print("5. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            p1a.p1a()
        elif choice == '2':
            stari = int(input("Introduceti numarul de stari: "))
            p1b.p1b(stari)
        elif choice == '3':
            p2a.p2a()
        elif choice == '4':
            bleu.bleu()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == '__main__':
    main()
