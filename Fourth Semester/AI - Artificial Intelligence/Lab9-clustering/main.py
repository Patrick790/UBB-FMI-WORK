import BagOfWords
import Doc2Vec
import emotii
import kmeans


def print_menu():
    print("1. Run Bag of Words")
    print("2. Run Doc2Vec")
    print("3. Run Emotii")
    print("4. Run KMeans")
    print("5. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            BagOfWords.bag_of_words()
        elif choice == '2':
            Doc2Vec.doc2vec()
        elif choice == '3':
            emotii.emotion_labeling()
        elif choice == '4':
            kmeans.emotion_labeling()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == '__main__':
    main()
