class LibrarySystem:
    def __init__(self):
        self.books = {
            'Book A': True,
            'Book B': True,
            'Book C': True,
            'Book D': True,
            'Book E': True
        }

    def check_out_book(self, book_name):
        if book_name in self.books:
            if self.books[book_name]:
                self.books[book_name] = False
                print(f"{book_name} 도서가 대출되었습니다.")
            else:
                print(f"{book_name} 도서는 이미 대출중입니다.")
        else:
            print(f"{book_name} 도서는 도서 목록에 없습니다.")

    def return_book(self, book_name):
        if book_name in self.books:
            if not self.books[book_name]:
                self.books[book_name] = True
                print(f"{book_name} 도서가 반납되었습니다.")
            else:
                print(f"{book_name} 도서는 이미 반납되었습니다.")
        else:
            print(f"{book_name} 도서는 도서 목록에 없습니다.")

    def view_books(self):
        print("도서 목록:")
        for book, available in self.books.items():
            status = "대출 가능" if available else "대출 중"
            print(f"{book}: {status}")

if __name__ == "__main__":
    system = LibrarySystem()

    while True:
        print("\n1. 도서 대출하기")
        print("2. 도서 반납하기")
        print("3. 도서 목록 보기")
        print("4. 종료하기")
        choice = int(input("원하는 작업을 선택하세요: ").strip())

        if choice == 1:
            book_name = input("대출할 도서 이름: ").strip()
            system.check_out_book(book_name)
        elif choice == 2:
            book_name = input("반납할 도서 이름: ").strip()
            system.return_book(book_name)
        elif choice == 3:
            system.view_books()
        elif choice == 4:
            print("시스템을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
