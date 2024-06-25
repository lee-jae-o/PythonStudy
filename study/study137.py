class ExpenseTracker:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_income(self, amount, description):
        self.balance += amount
        self.transactions.append((amount, description, "수입"))

    def add_expense(self, amount, description):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append((-amount, description, "지출"))
        else:
            print("잔액이 부족하여 지출할 수 없습니다.")

    def view_balance(self):
        print(f"현재 잔액: {self.balance}원")

    def view_transactions(self):
        print("거래 내역:")
        for amount, description, trans_type in self.transactions:
            print(f"{trans_type}: {description} - {amount}원")

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\n1. 수입 추가하기")
        print("2. 지출 추가하기")
        print("3. 잔액 확인하기")
        print("4. 거래 내역 보기")
        print("5. 종료하기")
        choice = int(input("원하는 작업을 선택하세요: ").strip())

        if choice == 1:
            amount = int(input("수입 금액: ").strip())
            description = input("수입 설명: ").strip()
            tracker.add_income(amount, description)
        elif choice == 2:
            amount = int(input("지출 금액: ").strip())
            description = input("지출 설명: ").strip()
            tracker.add_expense(amount, description)
        elif choice == 3:
            tracker.view_balance()
        elif choice == 4:
            tracker.view_transactions()
        elif choice == 5:
            print("시스템을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
