class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            return f"'{username}'은(는) 이미 등록된 사용자입니다."
        self.users[username] = password
        return f"'{username}' 사용자가 등록되었습니다."

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return f"'{username}' 사용자로 로그인되었습니다."
        return "잘못된 사용자 이름 또는 비밀번호입니다."

    def change_password(self, username, old_password, new_password):
        if username in self.users and self.users[username] == old_password:
            self.users[username] = new_password
            return f"'{username}' 사용자의 비밀번호가 변경되었습니다."
        return "잘못된 사용자 이름 또는 비밀번호입니다."

if __name__ == "__main__":
    user_manager = UserManager()

    while True:
        print("\n무슨 작업을 하시겠습니까? (회원가입, 로그인, 비밀번호 변경, 종료): ")
        action = input().strip()

        if action == "종료":
            break

        if action == "회원가입":
            username = input("사용자 이름을 입력하세요: ").strip()
            password = input("비밀번호를 입력하세요: ").strip()
            print(user_manager.register_user(username, password))
        elif action == "로그인":
            username = input("사용자 이름을 입력하세요: ").strip()
            password = input("비밀번호를 입력하세요: ").strip()
            print(user_manager.login(username, password))
        elif action == "비밀번호 변경":
            username = input("사용자 이름을 입력하세요: ").strip()
            old_password = input("현재 비밀번호를 입력하세요: ").strip()
            new_password = input("새로운 비밀번호를 입력하세요: ").strip()
            print(user_manager.change_password(username, old_password, new_password))
        else:
            print("잘못된 작업입니다. '회원가입', '로그인', '비밀번호 변경', '종료'를 입력하세요.")
