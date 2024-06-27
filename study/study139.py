class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - 전화번호: {self.phone}, 이메일: {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"{name}님의 연락처가 추가되었습니다.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"{name}님의 연락처가 삭제되었습니다.")
                return
        print("해당 이름의 연락처가 없습니다.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print("해당 이름의 연락처가 없습니다.")

    def view_contacts(self):
        if not self.contacts:
            print("연락처 목록이 비어 있습니다.")
        else:
            print("연락처 목록:")
            for contact in self.contacts:
                print(contact)

if __name__ == "__main__":
    manager = ContactManager()

    while True:
        print("\n1. 연락처 추가하기")
        print("2. 연락처 삭제하기")
        print("3. 연락처 검색하기")
        print("4. 연락처 목록 보기")
        print("5. 종료하기")
        choice = int(input("원하는 작업을 선택하세요: ").strip())

        if choice == 1:
            name = input("이름: ").strip()
            phone = input("전화번호: ").strip()
            email = input("이메일: ").strip()
            manager.add_contact(name, phone, email)
        elif choice == 2:
            name = input("삭제할 연락처 이름: ").strip()
            manager.remove_contact(name)
        elif choice == 3:
            name = input("검색할 연락처 이름: ").strip()
            manager.search_contact(name)
        elif choice == 4:
            manager.view_contacts()
        elif choice == 5:
            print("시스템을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
