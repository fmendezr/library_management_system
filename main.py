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
        self.burrowed = False
    
    def burrow_book(self, book):
        if not book.borrowed:
            book.borrowed = True
            print(f"Success! {book.title} by {book.author} has been burrowed.")
        else:
            print(f"{book.title} by {book.author} has already been burrowed.")

    def return_book(self, book):
        if book.burrowed:
            book.burrowed = False
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
                print(f"{book.title} by {book.author}")
        else:
            print("Library is empty.")
