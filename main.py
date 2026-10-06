#Assignment 1
#Student Name: Paulo Aunor
#Student Number: 9092305
#Email: raunor2305@conestogac.on.ca

from .utils import *

#initialize the Catalog and Cart
catalog = Catalog()
cart = Cart()

#function to display and get the prompts for 
#Add Book to Catalog
def add_book_to_catalog():
  #prompt user for isbn, title and author
  isAllInputValid = False
  while not isAllInputValid:
    isbn = input("Enter Book ISBN: ")
    #check if there is an existing isbn in the catalog
    #if yes, re-prompt for another ISBN
    if catalog.get_book_by_isbn(isbn):
      print("A book with ISBN {isbn} is already in the catalog")
      continue

    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")

    #adding the book to the catalog
    catalog.add_to_catalog()
    