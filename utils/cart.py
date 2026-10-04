#Student Name: Paulo Aunor
#Student Number: 9092305
#Email: raunor2305@conestogac.on.ca

#import BookNode class
from .bookNode import BookNode

#a class of the Cart (stack) objects that maintain a 
#head node, tail node and a length property
class Cart:
    #initialize a new empty Cart
    def __init__(self):
        self.__top = None
        self.__size = 0

    #add a new book to the top of the cart (head)
    def add_to_cart(self, book_data):
        new_book = BookNode(book_data)

        #if empty, assign new book to top
        if self.__size == 0:
            self.__top = new_book
        #else, rewire new book to top
        else:
            new_book.next = self.__top
            self.__top = new_book

        #increase cart length by 1 and return the 
        #updated stack
        self.__size += 1
        return self

    #returns the size of the cart
    def cart_size(self):
        return self.__size

    #returns the data value of the top book on the stack
    #w/o removing it. return None if empty
    def peek_cart(self):
        if self.__size == 0:
            return None
        return self.__top.book_data

    #returns true if cart is empty
    #false otherwise
    def is_cart_empty(self):
        return self.__size == 0

    #remove and return the last book added
    #or None if empty
    def remove_from_cart(self):
        #if empty return none:
        if self.__size == 0:
            return None

        #create temp_book and put the current top there
        #rewire the current top's next to the top of the stack
        temp_book = self.__top
        self.__top = self.__top.next

        #decrease size by 1 and return temp's data
        self.__size -= 1
        return temp_book.book_data


        


