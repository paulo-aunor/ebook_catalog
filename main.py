#Assignment 1
#Student Name: Paulo Aunor
#Student Number: 9092305
#Email: raunor2305@conestogac.on.ca

from utils import *
from helpers import *

#initialize the Catalog and Cart
catalog = Catalog()
cart = Cart()

#main functions
#asks for user input and directs it to the correct processes
def process_menu_input():
  user_input = int(input("Enter the menu number from 1 - 11: "))
  match(user_input):
    case 1:
      #add book to catalog
      add_book_to_catalog(catalog)
    case 2:
      #display catalog
      print("====Catalog====")
      print(catalog)
    case 3:
      #get books by author
      author = input("Enter Author Name: ")
      books_found = catalog.get_books_by_author(author)

      #check if books_found is empty
      if not books_found:
        print("No books by {author}")
      else:
        #iterrate through all book nodes and show them
        for book in books_found:
          print(str(book.book_data))
    case 4:
      #get book by title
      title = input("Enter Book Title: ")
      books_found = catalog.get_books_by_title(title)

      #check if books_found is empty
      if not books_found:
        print("No books with that title")
      else:
        print(f"Books titled {title}..")
        #iterrate through all book nodes and show them
        for book in books_found:
          book_data = book.book_data
          print(f'"{book_data.title}" (ISBN: {book_data.isbn})')
    case 5:
      #get book by isbn
      isbn = input("Enter ISBN: ")
      book_found = catalog.get_book_by_isbn(isbn)

      #check if book_found is empty
      if not book_found:
        print("No book found with that ISBN")
      else:
        book_data = book_found.book_data
        print(f'Found {book_data.title} by {book_data.author}')
    case 6:
        #remove book by isbn
        isbn = input("Enter ISBN to remove: ")
        book_found = catalog.remove_book_by_isbn(isbn)

        #check if book_found is empty
        if not book_found:
          print("No book found with that ISBN")
        else:
          book_data = book_found.book_data
          print(f'Removed {book_data.title} by {book_data.author}')
    case 7:
      #add book to checkout cart
      title = input("Enter book title to add to checkout: ")
      book_to_add = catalog.get_books_by_title(title)

      #check if book_to_add is empty
      if not book_to_add:
        print("No books of that title in the catalog")
      else:
        book_data = book_to_add[0].book_data
        cart.add_to_cart(book_data)
        print(f'Book "{title}" added to cart')

    case _:
      print("Invalid input")

running = True    
while running:
  #display menu
  display_menu()
  process_menu_input()