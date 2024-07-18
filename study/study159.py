class UserManager:
    def __init__(self):
        self.user_info = {}

    def add_user(self, name, age, email):
        if name in self.user_info:
            print(f"오류: {name}는(은) 이미 등록된 사용자입니다.")
        else:
            self.user_info[name] = {'age': age, 'email': email}
            print(f"{name}님의 정보가 성공적으로 등록되었습니다.")

    def view_user(self, name):
        if name in self.user_info:
            age = self.user_info[name]['age']
            email = self.user_info[name]['email']
            print(f"이름: {name}, 나이: {age}, 이메일: {email}")
        else:
            print(f"오류: {name}에 대한 정보를 찾을 수 없습니다.")

    def update_user(self, name, age=None, email=None):
        if name in self.user_info:
            if age:
                self.user_info[name]['age'] = age
            if email:
                self.user_info[name]['email'] = email
            print(f"{name}님의 정보가 업데이트되었습니다.")
        else:
            print(f"오류: {name}에 대한 정보를 찾을 수 없습니다.")

def main():
    manager = UserManager()
    while True:
        print("\n1. 사용자 등록")
        print("2. 사용자 조회")
        print("3. 사용자 정보 업데이트")
        print("4. 종료")
        choice = input("원하는 작업 번호를 입력하세요: ")

        if choice == '1':
            name = input("이름을 입력하세요: ")
            age = int(input("나이를 입력하세요: "))
            email = input("이메일을 입력하세요: ")
            manager.add_user(name, age, email)
        elif choice == '2':
            name = input("조회할 사용자의 이름을 입력하세요: ")
            manager.view_user(name)
        elif choice == '3':
            name = input("정보를 업데이트할 사용자의 이름을 입력하세요: ")
            age = input("새로운 나이(변경하지 않을 경우 엔터): ")
            email = input("새로운 이메일(변경하지 않을 경우 엔터): ")
            age = int(age) if age else None
            manager.update_user(name, age, email)
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
