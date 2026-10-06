#Student Name: Paulo Aunor
#Student Number: 9092305
#Email: raunor2305@conestogac.on.ca

#import BookNodeCatalog from bookNode.py
from .bookNode import BookNodeCatalog, Book

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
            book_strings.append(str(current_book.book_data))

            #move current book to the next
            current_book = current_book.next

        #return the string format
        return "|--|" + "<-->".join(book_strings) + "--|"


    #method to add a book to the Catalog, grouped by author
    #if the author already exists, insert after their last book
    #else add to the end
    #ISBNs are unique
    def add_to_catalog(self, isbn, title, author):
        #create a new BookNodeCatalog
        new_book_data = Book(isbn, title, author)
        new_book_node = BookNodeCatalog(new_book_data)

        #if catalog is empty, set both head and tail to point
        #at the new book
        if self.length == 0:
            self.head = new_book_node
            self.tail = new_book_node
        else:
            insert_after_book = None
            current_book =  self.head

            #traverse the whole list. Every time the author's name
            #comes up, update the "insert_after_book"
            while current_book:
                if current_book.book_data.author.lower() == author.lower():
                    insert_after_book = current_book
                current_book = current_book.next

            #if the author is found and it's not the last book in the catalog
            if insert_after_book is not None and insert_after_book != self.tail:
                next_book = insert_after_book.next

                #wire the new book to the target book
                insert_after_book.next = new_book_node
                new_book_node.previous = insert_after_book

                #wire the new book to the next node
                new_book_node.next = next_book
                next_book.previous = new_book_node
            else:
                self.tail.next = new_book_node
                new_book_node.previous = self.tail
                self.tail = new_book_node

        #increase the length by 1 and return the 
        #updated list
        self.length += 1
        return self

    #returns all books by author. None if catalog is empty
    def get_books_by_author(self, author):
        #if empty, return None
        if self.length == 0:
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
            if current_book.book_data.author.lower() == author.lower():
                authored_books.append(current_book)
            current_book = current_book.next

        #return the authored_books list
        return authored_books

    #returns all books by a given title. None if catalog is empty
    def get_books_by_title(self, title):
        #if empty, return None
        if self.length == 0:
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
            if title.lower() in current_book.book_data.title.lower() :
                titled_books.append(current_book)
            current_book = current_book.next

        #return the titled_books list
        return titled_books

    #returns book by a given isbn. None if catalog is empty
    def get_book_by_isbn(self, isbn):
        #if empty, return None
        if self.length == 0:
            return None

        #else, traverse through catalog
        #set current head of the catalog as the current book
        current_book = self.head

        #traverse list while current_book is not null
        #return the current book if it contains the required title
        #then set the current book's next as the new current book
        while current_book:
            if isbn.lower() == current_book.book_data.isbn.lower() :
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
            if isbn.lower() == current_book.book_data.isbn.lower() :
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

                #decrease the length of the catalog
                self.length -= 1    
                return found_book  

            current_book = current_book.next

        #return None if there are no matches
        return None

    

    
