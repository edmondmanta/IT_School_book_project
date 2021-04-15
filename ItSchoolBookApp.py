#
def add_book():
    book_name = input("Insert a book name -> ")
    author_name = input("Insert a author name -> ")
    # importing CSV lib
    import csv
    with open('booksDB.csv', 'w') as file:
        writer = csv.DictWriter(file,fieldnames=[
            'BookName','AuthorName','SharedWith','IsRead'
        ])
        writer.writerow({'BookName': book_name,
                         'AuthorName': author_name
                         })
    print('Book was added successfully ')




def list_book():
    print("List books option")
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
