class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book Added Successfully!")

    def show_books(self):
        if len(self.books) == 0:
            print("No Books Available")
        else:
            print("\nAvailable Books:")
            print(self.books)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book Issued Successfully!")
        else:
            print("Book Not Available")

    def return_book(self, book):
        self.books.append(book)
        print("Book Returned Successfully!")

