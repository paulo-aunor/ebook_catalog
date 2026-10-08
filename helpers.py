#Assignment 1
#Student Name: Paulo Aunor
#Student Number: 9092305
#Email: raunor2305@conestogac.on.ca

#python file containing all helper functions used in
#main.py

from utils import *

#function to display the menu
def display_menu():
  print("=================================")
  print("===Welcome to my ebook store!====")
  print("===Select a number from 1 to 11==")
  print("1. Add book to Catalog")
  print("2. Display Catalog")
  print("3. Search Book by Author")
  print("4. Search Book by Title")
  print("5. Search Book by ISBN")
  print("6. Remove Book by ISBN")
  print("7. Add Book to Checkout Cart")
  print("8. Remove Book from Cart")
  print("9. Peek Cart")
  print("10. Display Cart Size")
  print("11. Exit Program")

#function to display and get the prompts for 
#Add Book to Catalog
def add_book_to_catalog(catalog: Catalog):
  #prompt user for isbn, title and author
  isAllInputValid = False
  while not isAllInputValid:
    isbn = input("Enter Book ISBN: ")
    #check if there is an existing isbn in the catalog
    #if yes, re-prompt for another ISBN
    if catalog.get_book_by_isbn(isbn):
      print("A book with ISBN {isbn} is already in the collection")
      continue

    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")

    #adding the book to the catalog
    catalog.add_to_catalog(isbn, title, author)
    print(f"Book '{title}' by {author} added successfully")
    isAllInputValid = True
