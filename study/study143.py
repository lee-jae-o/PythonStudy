import os
import json
from datetime import datetime

class BirthdayManager:
    def __init__(self, filename):
        self.filename = filename
        self.birthdays = {}
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.birthdays = json.load(file)

    def add_birthday(self, name, birthdate):
        self.birthdays[name] = birthdate
        self.save()
        print(f"{name}의 생일이 {birthdate}로 추가되었습니다.")

    def remove_birthday(self, name):
        if name in self.birthdays:
            del self.birthdays[name]
            self.save()
            print(f"{name}의 생일이 삭제되었습니다.")
        else:
            print(f"{name}의 생일 정보가 없습니다.")

    def view_birthday(self, name):
        if name in self.birthdays:
            print(f"{name}의 생일은 {self.birthdays[name]}입니다.")
        else:
            print(f"{name}의 생일 정보가 없습니다.")

    def upcoming_birthdays(self):
        today = datetime.today().strftime('%m-%d')
        upcoming = {name: date for name, date in self.birthdays.items() if date >= today}
        if upcoming:
            print("다가오는 생일들:")
            for name, date in sorted(upcoming.items(), key=lambda x: x[1]):
                print(f"{name}: {date}")
        else:
            print("다가오는 생일이 없습니다.")

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.birthdays, file)

def main():
    manager = BirthdayManager('birthdays.json')

    while True:
        print("\n친구 생일 관리 프로그램")
        print("1. 생일 추가")
        print("2. 생일 삭제")
        print("3. 생일 확인")
        print("4. 다가오는 생일 보기")
        print("5. 종료")
        choice = input("선택: ").strip()

        if choice == '1':
            name = input("친구의 이름을 입력하세요: ")
            birthdate = input("생일을 MM-DD 형식으로 입력하세요 (예: 07-15): ")
            manager.add_birthday(name, birthdate)
        elif choice == '2':
            name = input("삭제할 친구의 이름을 입력하세요: ")
            manager.remove_birthday(name)
        elif choice == '3':
            name = input("확인할 친구의 이름을 입력하세요: ")
            manager.view_birthday(name)
        elif choice == '4':
            manager.upcoming_birthdays()
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
