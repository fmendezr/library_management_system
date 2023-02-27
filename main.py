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