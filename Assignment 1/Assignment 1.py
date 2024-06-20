import csv

FILENAME = 'books.csv'


def display_welcome():
    print("Books To Read 1.0 - by [Your Name]")


def load_books(filename):
    books = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row[2] = int(row[2])  # Convert pages to int
                books.append(row)
        print(f"{len(books)} books loaded from {filename}.")
    except FileNotFoundError:
        print(f"File {filename} not found, starting with an empty book list.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return books


def display_menu():
    menu = """
Menu:
D - Display books
A - Add new book
C - Complete a book
Q - Quit
>>> """
    return input(menu).strip().upper()


def display_books(books):
    if not books:
        print("No books available.")
        return
    books.sort(key=lambda book: (book[1], book[0]))  # Sort by author, then title
    unread_count = 0
    total_pages = 0
    for i, book in enumerate(books, 1):
        status = "*" if book[3] == 'u' else " "
        print(f"{status}{i}. {book[0]:<40} by {book[1]:<20} {book[2]:>4} pages")
        if book[3] == 'u':
            unread_count += 1
            total_pages += book[2]
    print(f"You need to read {unread_count} books totaling {total_pages} pages.")


def add_book(books):
    title = input("Title: ").strip()
    while not title:
        print("Input cannot be blank")
        title = input("Title: ").strip()

    author = input("Author: ").strip()
    while not author:
        print("Input cannot be blank")
        author = input("Author: ").strip()

    pages = input("Number of Pages: ").strip()
    while not pages.isdigit() or int(pages) <= 0:
        print("Invalid input; enter a valid number of pages")
        pages = input("Number of Pages: ").strip()
    pages = int(pages)

    books.append([title, author, pages, 'u'])
    print(f"{title} by {author} ({pages} pages) added.")


def complete_book(books):
    if not books:
        print("No books available.")
        return
    unread_books = [book for book in books if book[3] == 'u']
    if not unread_books:
        print("No unread books to mark as completed.")
        return

    display_books(books)
    book_number = input("Enter the number of a book to mark as completed: ").strip()
    while not book_number.isdigit() or int(book_number) <= 0 or int(book_number) > len(books):
        print("Invalid input; enter a valid book number")
        book_number = input("Enter the number of a book to mark as completed: ").strip()
    book_number = int(book_number)
    if books[book_number - 1][3] == 'c':
        print("That book is already completed")
    else:
        books[book_number - 1][3] = 'c'
        print(f"{books[book_number - 1][0]} by {books[book_number - 1][1]} marked as completed!")


def save_books(filename, books):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for book in books:
                writer.writerow(book)
        print(f"{len(books)} books saved to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    books = load_books(FILENAME)
    display_welcome()
    while True:
        choice = display_menu()
        if choice == 'D':
            display_books(books)
        elif choice == 'A':
            add_book(books)
        elif choice == 'C':
            complete_book(books)
        elif choice == 'Q':
            save_books(FILENAME, books)
            print('Goodbye!')
            break
        else:
            print("Invalid menu choice")


if __name__ == '__main__':
    main()
