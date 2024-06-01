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
    books = ["파이썬", "자바", "C", "C++", "C#"]
    library = Library(books)

    while True:
        print("\n도서관 도서 목록:")
        for book, available in library.books.items():
            status = "대출 가능" if available else "대출 중"
            print(f"{book}: {status}")

        action = input("\n무슨 작업을 하시겠습니까? (대출, 반납, 종료): ").strip()

        if action == "종료":
            break

        book_name = input("도서 이름을 입력하세요: ").strip()

        if action == "대출":
            print(library.borrow_book(book_name))
        elif action == "반납":
            print(library.return_book(book_name))
        else:
            print("잘못된 작업입니다. '대출' 또는 '반납'을 입력하세요.")