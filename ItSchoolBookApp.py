#
def add_book():
    book_name = input("Insert a book name -> ")
    author_name = input("Insert a author name -> ")
    # importing CSV lib
    import csv
    with open('booksDB.csv', mode='w') as file:
        writer = csv.DictWriter(file,fieldnames=[
            'BookName','AuthorName','SharedWith','IsRead'
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
        rows = csv.DictReader(file,fieldnames=[
            'BookName','AuthorName','SharedWith','IsRead'
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
    print("Update a book option")
def share_book():
    print("Share a book option")


# Main menu for user
print('Menu: ')
print('1: Add a book')
print('2: List books')
print('3: Update a book')
print('4: Share a book')

option = int(input("Select one option -> "))

if option == 1:
    add_book()
elif option == 2:
    list_book()
elif option == 3:
    update_book()
elif option == 4:
    share_book()
else:
    print("Not a valid option")
