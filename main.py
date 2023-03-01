import csv

with open("books.csv", "r", newline="\n") as read_list_of_books:
    reader = csv.reader(read_list_of_books, delimiter=",")
    csv_list = []
    for row in reader:
        csv_list.append(row)
    read_list_of_books.close()
    
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
    
    def burrow_book(self, book):
        if not self.borrowed:
            self.borrowed = True
            print(f"Success! {book.title} by {book.author} has been burrowed.")
        else:
            print(f"{book.title} by {book.author} has already been burrowed.")

    def return_book(self, book):
        if self.borrowed:
            self.borrowed = False
            print(f"Success! {book.title} by {book.author} has been returned.")
        else:
            print(f"{book.title} by {book.author} has not been burrowed.")

class Library:
    def __init__(self):
        self.library_list = []
        for book in csv_list:
            self.library_list.append(Book(book[0], book[1]))
    
    def add_book(self, new_book):
        self.library_list.append(new_book)
        print(f"{new_book.title} by {new_book.author} has been added to the library successfully.")

    def list_books(self):
        print("Here is a list of the books available in the library: ")
        if len(self.library_list) >  0:
            for book in self.library_list:
                print(f"\t-{book.title} by {book.author}")
        else:
            print("Library is empty.")


def update_library_csv(b_title, b_author):
    with open("books.csv", "a", newline="\n") as write_list_of_books:
        writer = csv.writer(write_list_of_books)
        writer.writerow([b_title, b_author])
    write_list_of_books.close()

print("\nWelcome to the best library management system")
print("There are the things thtat you can do\n1. List of Books in the library \n2. Add a book \n3. Borrow a book \n4. Return the book"
)

library = Library()

ans = "Y"

while True:
    if ans == "Y":
        anss = (input("\nEnter a number: ")).strip()
        print("")
        if anss == "1":
            library.list_books()
        elif anss == "2":
            b_title = input("Enter book's title: ")
            b_author = input("Enter book's author: ")
            library.add_book(Book(b_title, b_author))
            update_library_csv(b_title, b_author)
        elif anss == "3":
            b_title = input("Enter book's title: ")
            b_author = input("Enter book's author: ")
            for book in library.library_list:
                if book.title == b_title:
                    book.burrow_book(Book(b_title, b_author))
                    break
            else:
                print("Book does not exist")

        elif anss == "4":
            b_title = input("Enter book's title: ")
            b_author = input("Enter book's author: ")
            for book in library.library_list:
                if book.title == b_title:
                    book.return_book(Book(b_title, b_author))
                    break
            else:
                print("Book does not exist") 
        else:
            print("Invalid input")
    elif ans == "N":
        print("\nThank you! See ya soon\n")
        break
    else:
        print("\nInvalid input")
    
    ans = input("\nDo you wish to continue (Y or N): ")

    