class FinanceManager:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_transaction(self, amount, description):
        self.balance += amount
        self.transactions.append((amount, description))
        print(f"거래 내역: {description}, 금액: {amount}원. 현재 잔액: {self.balance}원.")

    def show_balance(self):
        print(f"현재 잔액은 {self.balance}원 입니다.")

    def list_transactions(self):
        if not self.transactions:
            print("거래 내역이 없습니다.")
        else:
            print("거래 내역 목록:")
            for amount, description in self.transactions:
                transaction_type = "입금" if amount > 0 else "출금"
                print(f"{transaction_type}: {description}, 금액: {amount}원")

def main():
    manager = FinanceManager()
    while True:
        print("\n1. 거래 내역 추가")
        print("2. 잔액 확인")
        print("3. 거래 내역 보기")
        print("4. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            amount = float(input("거래 금액을 입력하세요 (입금은 +, 출금은 -로 표시): "))
            description = input("거래 설명을 입력하세요: ")
            manager.add_transaction(amount, description)
        elif choice == '2':
            manager.show_balance()
        elif choice == '3':
            manager.list_transactions()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
