class EventManager:
    def __init__(self):
        self.attendees = []

    def add_attendee(self, name, email, age):
        if any(attendee['email'] == email for attendee in self.attendees):
            print(f"오류: 이미 등록된 이메일 주소입니다. {email}")
        else:
            self.attendees.append({'name': name, 'email': email, 'age': age})
            print(f"{name}님을 참석자 목록에 추가했습니다.")

    def list_attendees(self):
        if not self.attendees:
            print("참석자 목록이 비어 있습니다.")
        else:
            print("참석자 목록:")
            for attendee in self.attendees:
                print(f"이름: {attendee['name']}, 이메일: {attendee['email']}, 나이: {attendee['age']}")

    def filter_attendees_by_age(self, minimum_age):
        filtered = [attendee for attendee in self.attendees if attendee['age'] >= minimum_age]
        if not filtered:
            print(f"{minimum_age}세 이상인 참석자가 없습니다.")
        else:
            print(f"{minimum_age}세 이상인 참석자 목록:")
            for attendee in filtered:
                print(f"이름: {attendee['name']}, 이메일: {attendee['email']}, 나이: {attendee['age']}")

def main():
    manager = EventManager()
    while True:
        print("\n1. 참석자 추가")
        print("2. 참석자 목록 보기")
        print("3. 특정 나이 이상 참석자 필터링")
        print("4. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            name = input("참석자 이름을 입력하세요: ")
            email = input("참석자 이메일을 입력하세요: ")
            age = int(input("참석자 나이를 입력하세요: "))
            manager.add_attendee(name, email, age)
        elif choice == '2':
            manager.list_attendees()
        elif choice == '3':
            minimum_age = int(input("필터링할 최소 나이를 입력하세요: "))
            manager.filter_attendees_by_age(minimum_age)
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
