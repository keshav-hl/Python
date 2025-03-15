#Optional Parameters in Constructors/
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

    def show_book(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("Python Programming")
book2 = Book("Machine Learning", "Andrew Ng")

book1.show_book()
book2.show_book()