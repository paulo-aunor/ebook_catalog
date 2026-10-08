#Student Name: Paulo Aunor
#Student Number: 9092305
#Email: raunor2305@conestogac.on.ca

class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    #string override to make the output data readable
    def __str__(self):
        return f'"{self.title}" by {self.author} (ISBN: {self.isbn})'

#a class of BookNode objects that contain a data value
#and a references to the next book in the list
#or none if there's no next Book
class BookNode:
    def __init__(self, book_data):
        self.book_data = book_data
        self.next = None


#a class of BookNodeCatalog objects that contain an isbn, title, author and
#and a references to the previous and next book in the list
#or none if there's no next Book
class BookNodeCatalog:
    def __init__(self, book: Book):
        self.book_data = book
        self.previous = None
        self.next = None