import csv

with open("books.csv", "r", newline="\n") as read_list_of_books:
    reader = csv.reader(read_list_of_books, delimiter=",")
    csv_list = []
    for row in reader:
        csv_list.append(row)
    read_list_of_books.close()
    