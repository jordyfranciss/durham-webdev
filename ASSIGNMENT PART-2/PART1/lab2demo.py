import os
import csv


def main():
    book_list = []

    if not os.path.exists('book.csv'):
        with open('book.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Title', 'Author', 'Year'])
            writer.writeheader()

    while True:
        print("Reading list management")
        print("1. Add a new book\n2. List all the books\n3. Search for a book\n4. Exit program")
        choice_from_user = input("Enter your choice: ")

        if choice_from_user == '1':
            add_books(book_list)
        elif choice_from_user == '2':
            list_books(book_list)
        elif choice_from_user == '3':
            search_book(book_list)
        elif choice_from_user == '4':
            exit("The program has been withdrawn")


def search_book(book_list):
    title = input("Enter the title of the book: ")
    found = False

    for book in book_list:
        if book['Title'].lower() == title.lower():
            print(f"Book found: {book['Title']} by the {book['Author']} published year {book['Year']}")
            found = True
            break
    if not found:
        print("Book is not found in the list")


def add_books(book_list):
    new_title = input("Enter title: ")
    new_year = input("Enter year: ")
    new_author = input("Enter author name: ")

    new_book = {'Title': new_title, 'Author': new_author, 'Year': new_year}
    book_list.append(new_book)


def list_books(book_list):
    for index, book in enumerate(book_list):
        print(f"{index + 1}. {book['Title']} by {book['Author']} published in {book['Year']}")


if __name__ == "__main__":
    main()
