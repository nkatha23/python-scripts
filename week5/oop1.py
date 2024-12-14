# Base Class: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

    def read(self):
        return f"You're reading '{self.title}'."

# Derived Class: EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    # Overriding description to include file size
    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages, {self.file_size} MB eBook."

    def read(self):
        return f"You're reading '{self.title}' on your e-reader."

# Example Usage
physical_book = Book("1984", "George Orwell", 328)
ebook = EBook("Sapiens", "Yuval Noah Harari", 464, 2)

print(physical_book.description())
print(physical_book.read())
print(ebook.description())
print(ebook.read())
