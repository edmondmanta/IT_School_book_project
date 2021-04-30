#
def add_book():
    book_name = input("Insert a book name -> ")
    author_name = input("Insert a author name -> ")
    # importing CSV lib
    import csv
    with open('booksDB.csv', mode='a') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'BookName', 'AuthorName', 'SharedWith', 'IsRead'
        ])
        writer.writerow({'BookName': book_name,
                         'AuthorName': author_name,
                         'SharedWith': 'None',
                         'IsRead': False
                         })
    print('Book was added successfully ')


def list_book():
    import csv
    with open('booksDB.csv', mode='r') as file:
        # Pasul 1 sa luam toate datele din DB
        rows = csv.DictReader(file, fieldnames=[
            'BookName', 'AuthorName', 'SharedWith', 'IsRead'
        ])
        # Parcurgem rand cu rand
        for row in rows:
            # pe o singura linie
            print(
                f"Book name is: {row.get('BookName')} "
                f"Author name is: {row.get('AuthorName')} "
                f"Is shared? {row.get('ShareWith')} "
                f"Is read? {row.get('IsRead',False)}")
        # rezultat pe mai multe linii
            # print(f"Book name is: {row.get('BookName')}")
            # print(f"Author Name is: {row.get('AuthorName')}")
            # print(f"The book is shared with: {row.get('ShareWith')}")
            # print(f"The book is read: {row.get('IsRead',False)}")


def update_book():
    book_name = input("Enter book name: ")
    book_read = input("Is the book read?(Y/N)?")
    if book_read == 'Y' or book_read.upper() == 'YES':
        book_read = True
    else:
        book_read = False
    import csv
    rows = []
    with open('booksDB.csv', mode='r') as file:
        # rows = list(csv.DictReader(file))
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead")))
        for row in rows:
            if row["BookName"] == book_name:
                row["IsRead"] = book_read
                break
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "BookName", "AuthorName", "SharedWith", "IsRead"
            ])
            csv_writer.writerow({"BookName": row.get("BookName"),
                                 "AuthorName": row.get("AuthorName"),
                                 "SharedWith": row.get("SharedWith"),
                                 "IsRead": book_read}
                                )
        print("Book was updated successfully")


def share_book():
    book_name = input("What is the name of the book you want to share-> ")
    shared_with = input('With whom do you want to share? -> ')
    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead")))
        for row in rows:
            if row["BookName"] == book_name:
                row["SharedWith"] = shared_with
                break
            else:
                print('Book is not in DB')
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "BookName", "AuthorName", "SharedWith", "IsRead"
            ])
            csv_writer.writerow({"BookName": row.get("BookName"),
                                 "AuthorName": row.get("AuthorName"),
                                 "SharedWith": shared_with,
                                 "IsRead": row.get("IsRead")}
                                )


def clear_csv():
    clear = open("booksDB.csv", "w")
    clear.truncate()
    clear.close()


# Main menu for user
print('Menu: ')
print('1: Add a book')
print('2: List books')
print('3: Update a book')
print('4: Share a book')
print('5: Delete all books')
print('6: Quit')


# while option != 5:
while True:
    option = int(input("Select one option -> "))
    if option == 1:
        add_book()
    elif option == 2:
        list_book()
    elif option == 3:
        update_book()
    elif option == 4:
        share_book()
    elif option == 5:
        clear_csv()
        break
    elif option == 6:
        break
    else:
        print("Not a valid option")
