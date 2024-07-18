class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다. 현재 잔액: {self.balance}원")
        else:
            print("입금 금액은 0보다 커야 합니다.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"{amount}원이 출금되었습니다. 현재 잔액: {self.balance}원")
            else:
                print("잔액이 부족합니다.")
        else:
            print("출금 금액은 0보다 커야 합니다.")

    def check_balance(self):
        print(f"현재 잔액: {self.balance}원")

def main():
    account = BankAccount()
    while True:
        print("\n1. 입금")
        print("2. 출금")
        print("3. 잔액 조회")
        print("4. 종료")
        choice = input("원하는 작업 번호를 입력하세요: ")

        if choice == '1':
            amount = float(input("입금할 금액을 입력하세요: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("출금할 금액을 입력하세요: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
