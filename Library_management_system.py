"""
1. Library Management System
Create:
Library
├── Book
├── Member
└── Librarian

Features:
Add books
Borrow books
Return books
Check availability
Track who borrowed which book

Concepts:
Composition
Encapsulation
Inheritance
"""

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True
        self.borrowed_by = None

class Member:
    def __init__(self, name):
        self.name = name

class Librarian(Member):
    def __init__(self, name):
        super().__init__(name)

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)
        print(f"{book.title} added successfully")

    def show_book(self):
        print("\nBooks In Library:")
        for i, book in enumerate(self.__books, start=1):
            print(f"{i}. {book.title}")

    def check_availability(self, title):
        print("\nAvailability State: ", end="")
        for book in self.__books:
            if book.title == title:
                if book.available:
                    print("Available")
                else:
                    print("Not Available")
                return
        print("This Book isn't in the library")

    def borrow_book(self, title, member):
        for book in self.__books:
            if book.title == title:
                if book.available:
                    book.available = False
                    book.borrowed_by = member.name
                    print(f"\n{member.name} borrowed {title}")
                else:
                    print("Book already borrowed")
                return
        print("Book not found")

    def return_book(self, title):
        for book in self.__books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    book.borrowed_by = None
                    print(f"\n{book.title} returned")
                else:
                    print("Book already returned")
                return
        print("Book not found")

    def track_books(self):
        print("\nBook Status:")
        for book in self.__books:
            if book.borrowed_by:
                print(f"{book.title} --> borrowed by {book.borrowed_by}")
            else:
                print(f"{book.title} --> Available")

book1 = Book("Python")
book2 = Book("Java")
book3 = Book("C++")
book4 = Book("HTML")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.show_book()

library.check_availability("CSS")
library.check_availability("Python")

mem1 = Member("Paban")
mem2 = Member("Hari")

library.borrow_book("Python", mem1)
library.borrow_book("HTML", mem2)

library.check_availability("Python")

library.return_book("Python")

library.track_books()