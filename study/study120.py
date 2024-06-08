class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        if name in self.contacts:
            return f"{name}은(는) 이미 주소록에 있습니다."
        self.contacts[name] = phone_number
        return f"{name}의 연락처가 추가되었습니다."

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return f"{name}의 연락처가 삭제되었습니다."
        return f"{name}을(를) 찾을 수 없습니다."

    def view_contacts(self):
        if not self.contacts:
            return "주소록이 비어 있습니다."
        
        contact_list = "현재 주소록:\n"
        for name, phone_number in sorted(self.contacts.items()):
            contact_list += f"{name}: {phone_number}\n"
        return contact_list.strip()

if __name__ == "__main__":
    address_book = AddressBook()

    while True:
        print("\n무슨 작업을 하시겠습니까? (추가, 삭제, 보기, 종료): ")
        action = input().strip()

        if action == "종료":
            break

        if action == "추가":
            name = input("이름을 입력하세요: ").strip()
            phone_number = input("전화번호를 입력하세요: ").strip()
            print(address_book.add_contact(name, phone_number))
        elif action == "삭제":
            name = input("삭제할 이름을 입력하세요: ").strip()
            print(address_book.delete_contact(name))
        elif action == "보기":
            print(address_book.view_contacts())
        else:
            print("잘못된 작업입니다. '추가', '삭제', '보기' 또는 '종료'를 입력하세요.")
