#Student Name: Paulo Aunor
#Student Number: 9092305
#Email: raunor2305@conestogac.on.ca

#import BookNodeCatalog from bookNode.py
from .bookNode import BookNodeCatalog

#a class of the Catalog objects that maintain a 
#head node, tail node and a length property
class Catalog:
    #initialize a new empty Catalog
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #converts the catalog to string
    def __str__(self):
        #return "Empty Catalog" if nothing inside
        if not self.head:
            return "Empty Catalog"

        #create an array for the book data strings
        #set the head of the catalog as the current book
        book_strings = []
        current_book = self.head

        #traverse the whole catalog
        while current_book:
            #convert the BookNodeCatalog object to string and store it
            book_strings.append(str(current_book))


    #method to add a book to the Catalog, grouped by author
    #if the author already exists, insert after their last book
    #else add to the end
    #ISBNs are unique
    def add_to_catalog(self, isbn, title, author):
        #create a new BookNodeCatalog
        new_book = BookNodeCatalog(isbn, title, author)

        #if catalog is empty, set both head and tail to point
        #at the new book
        if self.length == 0:
            self.head = new_book
            self.tail = new_book
        #else set the new book at the tail and tail's next, set the tail
        #to the new books's previous
        else:
            self.tail.next = new_book
            new_book.previous = self.tail
            self.tail = new_book

        #increase the length by 1 and return the 
        #updated list
        self.length += 1
        return self

    #returns all books by author. None if catalog is empty
    def get_books_by_author(self, author):
        #if empty, return None
        if self.__size == 0:
            return None

        #else, traverse through catalog
        #store books with chosen author in authored_books
        authored_books = []

        #set current head of the catalog as the current book
        current_book = self.head

        #traverse list while current_book is not null
        #append book to authored_books if it has the same author
        #then set the current book's next as the new current book
        while current_book:
            if current_book.author.lower() == author.lower():
                authored_books.append(current_book)
            current_book = current_book.next

        #return the authored_books list
        return authored_books

    #returns all books by a given title. None if catalog is empty
    def get_books_by_title(self, title):
        #if empty, return None
        if self.__size == 0:
            return None

        #else, traverse through catalog
        #store books with given title in titled_books
        titled_books = []

        #set current head of the catalog as the current book
        current_book = self.head

        #traverse list while current_book is not null
        #append book to titled_books if it contains the required title
        #then set the current book's next as the new current book
        while current_book:
            if title.lower() in current_book.title.lower() :
                titled_books.append(current_book)
            current_book = current_book.next

        #return the titled_books list
        return titled_books

    #returns book by a given isbn. None if catalog is empty
    def get_book_by_isbn(self, isbn):
        #if empty, return None
        if self.__size == 0:
            return None

        #else, traverse through catalog
        #set current head of the catalog as the current book
        current_book = self.head

        #traverse list while current_book is not null
        #return the current book if it contains the required title
        #then set the current book's next as the new current book
        while current_book:
            if isbn.lower() == current_book.isbn.lower() :
                return current_book
            current_book = current_book.next

        #return None if there are no matches
        return None

    #removes and returns a book by given isbn
    #return None if no matches
    def remove_book_by_isbn(self, isbn):
        #set current head of the catalog as the current head
        current_book = self.head

        #traverse list while current_book is not null
        while current_book:
            if isbn.lower() == current_book.isbn.lower() :
                found_book = current_book

                #update the catalog based on where the book was found
                #if current_book is at the head of the catalog
                if current_book == self.head:
                    self.head = current_book.next
                    #set the head's previous as None if the head is not null
                    if self.head:
                        self.head.previous = None
                    #else, set the tail as none as the catalog is empty
                    else:
                        self.tail = None
                #elif the current book is at the tail, 
                #rewire the current's previous as the new tail
                #set tail's next to None
                elif current_book == self.tail:
                    self.tail = current_book.previous
                    #if tail is not None, set tail's next as None
                    if self.tail:
                        self.tail.next = None

                #else if the current book is at the middle
                else:
                    current_book.previous.next = current_book.next
                    current_book.next.previous = current_book.previous

                return found_book  

            current_book = current_book.next

        #return None if there are no matches
        return None

    

    
