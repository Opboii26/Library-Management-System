class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.no_of_books = 0

    def updateTotalBooks(self):
        self.no_of_books = sum(value for book in self.books for value in book.values())

    def add_book(self, book):
        for i in self.books:
            if book in i:
                i[book] += 1
                self.updateTotalBooks()

        else:
            self.books.append({book: 1})
            self.updateTotalBooks()

    def add_book_stock(self, book, number_of_books):
        for i in self.books:
            if book in i:
                i[book] += number_of_books
                self.updateTotalBooks()

        else:
            self.books.append({book: number_of_books})
            self.updateTotalBooks()

    def showBooks(self, wantedBook):
        for i in self.books:
            if wantedBook in i:
                return f"Yes! {wantedBook} is available!\nTotal number of {wantedBook} is {i[wantedBook]}"

        else:
            return f"No! {wantedBook} is not available!"

    def totalBooks(self):
        return sum(value for book in self.books for value in book.values())

if __name__ == "__main__":
    Library = Library("Yash's library")

    Library.add_book_stock("Python", 20) # add 19 more python books
    Library.add_book_stock("Java", 10)
    Library.add_book("Python")

    print(Library.showBooks("Python"))
    print(Library.showBooks("Java"))
    print(Library.showBooks("C++"), "\n")

    print(Library.totalBooks())