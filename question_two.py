class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_information(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

# Creating an instance of the Book class
my_book = Book("White Christmas by", "Fortunate.Ogwal.R", 185)
print(my_book)

# Displaying the information of the book
my_book.display_information()

#derived class
class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def display_information(self):
        super().display_information()
        print(f"Format: {self.format}")

my_ebook = EBook("White Christmas by", "Fortunate.Ogwal.R", 185, "PDF")

my_ebook.display_information()

#Return book title and author
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_information(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def get_title_author(self):
        return f"Title: {self.title}, Author: {self.author}"

my_book = Book("White Christmas by", "Fortunate.Ogwal.R", 185,)

my_book.display_information()

# Getting only the title and author of the book use get() function
title_author = my_book.get_title_author()
print(title_author)

#Definition
#Class is an object constructor, or a "blueprint" for creating objects.
#an object has its own attributes