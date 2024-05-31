class Library:
    def __init__(self, books):
        self.books = {book: True for book in books}  

    def borrow_book(self, book):
        if book in self.books and self.books[book]:
            self.books[book] = False
            return f"'{book}' 도서가 대출되었습니다."
        elif book in self.books and not self.books[book]:
            return f"'{book}' 도서는 이미 대출 중입니다."
        else:
            return f"'{book}' 도서는 도서관에 없습니다."

    def return_book(self, book):
        if book in self.books and not self.books[book]:
            self.books[book] = True
            return f"'{book}' 도서가 반납되었습니다."
        elif book in self.books and self.books[book]:
            return f"'{book}' 도서는 대출되지 않았습니다."
        else:
            return f"'{book}' 도서는 도서관에 없습니다."

    def check_availability(self, book):
        if book in self.books:
            return self.books[book]
        else:
            return f"'{book}' 도서는 도서관에 없습니다."

if __name__ == "__main__":
    books = ["Python Programming", "Data Structures", "Algorithms", "Machine Learning", "Artificial Intelligence"]
    library = Library(books)

    print(library.borrow_book("Python Programming"))
    print(library.borrow_book("Python Programming"))
    print(library.return_book("Python Programming"))
    print(library.borrow_book("Python Programming"))
    print(library.check_availability("Data Structures"))
    print(library.borrow_book("Data Structures"))
    print(library.check_availability("Data Structures"))
    print(library.return_book("Data Structures"))
    print(library.return_book("Nonexistent Book"))