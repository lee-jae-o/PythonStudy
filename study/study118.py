class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount}원이 입금되었습니다. 현재 잔액: {self.balance}원"
        else:
            return "입금 금액은 0원보다 커야 합니다."

    def withdraw(self, amount):
        if amount > self.balance:
            return "잔액이 부족합니다."
        elif amount <= 0:
            return "출금 금액은 0원보다 커야 합니다."
        else:
            self.balance -= amount
            return f"{amount}원이 출금되었습니다. 현재 잔액: {self.balance}원"

    def check_balance(self):
        return f"현재 잔액: {self.balance}원"

if __name__ == "__main__":
    account = BankAccount("홍길동", 10000)

    while True:
        print("\n무슨 작업을 하시겠습니까? (입금, 출금, 잔액 확인, 종료): ")
        action = input().strip()

        if action == "종료":
            break

        if action == "입금":
            amount = int(input("입금할 금액을 입력하세요: ").strip())
            print(account.deposit(amount))
        elif action == "출금":
            amount = int(input("출금할 금액을 입력하세요: ").strip())
            print(account.withdraw(amount))
        elif action == "잔액 확인":
            print(account.check_balance())
        else:
            print("잘못된 작업입니다. '입금', '출금', '잔액 확인' 또는 '종료'를 입력하세요.")
