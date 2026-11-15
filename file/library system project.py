#                                      ---LIBRARY SYSTEM PROJECT--- 
books = []
FILE_NAME = "library.txt"
def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                book_id, title, author, status, member = line.split("|")
                book = {
                    "id": book_id,
                    "title": title,
                    "author": author,
                    "status": status,
                    "member": member,
                }
                books.append(book)
    except FileNotFoundError:
        pass

def save_books():
    with open(FILE_NAME, "w") as file:
        for book in books:
            line = book["id"] + "|" + book["title"] + "|" + book["author"] + "|" + book["status"] + "|" + book["member"]
            file.write(line + "\n")

def generate_id():
    if len(books) == 0:
        return "B101"
    highest = 100
    for book in books:
        number = int(book["id"][1:])  # "B101" -> 101
        if number > highest:
            highest = number
    return "B" + str(highest + 1)

def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def show_book(book):
    print(book["id"] + " | " + book["title"] + " | " + book["author"] + " | " + book["status"])

def count_available():
    count = 0
    for book in books:
        if book["status"] == "Available":
            count += 1
    return count

def add_book():
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    if title == "" or author == "":
        print("Title and author cannot be empty.")
        return
    book = {
        "id": generate_id(),
        "title": title,
        "author": author,
        "status": "Available",
        "member": "-",
    }
    books.append(book)
    print("Book added. ID: " + book["id"] + " | " + title + " | " + author + " | Available")

def issue_book():
    book_id = input("Book ID: ").strip().upper()
    book = find_book(book_id)
    if book is None:
        print("Book ID " + book_id + " not found.")
        return
    if book["status"] == "Issued":
        print("Book " + book_id + " is already issued.")
        return
    member = input("Member name: ").strip()
    if member == "":
        print("Member name cannot be empty.")
        return
    book["status"] = "Issued"
    book["member"] = member
    print("Book " + book_id + " issued to " + member + ". Status: Issued")
    print("Available books: " + str(count_available()))

def return_book():
    book_id = input("Book ID: ").strip().upper()
    book = find_book(book_id)
    if book is None:
        print("Book ID " + book_id + " not found.")
        return
    if book["status"] == "Available":
        print("Book " + book_id + " was not issued.")
        return
    book["status"] = "Available"
    book["member"] = "-"
    print("Book " + book_id + " returned. Status: Available")

def search_book():
    print("Search by: 1) Title  2) Author")
    choice = input("Choose: ").strip()
    if choice == "1":
        field = "title"
    elif choice == "2":
        field = "author"
    else:
        print("Invalid")
        return
    keyword = input("Enter search text: ").strip().lower()
    found = False
    for book in books:
        if keyword in book[field].lower():
            show_book(book)
            found = True
    if not found:
        print("No books found")

def display_all():
    if len(books) == 0:
        print("No books in the library")
        return
    for book in books:
        show_book(book)

def menu():
    print()
    print("*** LIBRARY MANAGEMENT SYSTEM ***")
    print("1. Add book")
    print("2. Issue book")
    print("3. Return book")
    print("4. Search book")
    print("5. Display all books")
    print("6. Exit")


def main():
    load_books()
    while True:
        menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            display_all()
        elif choice == "6":
            save_books()
            print("Data saved")
            break
        else:
            print("Invalid")
main()









