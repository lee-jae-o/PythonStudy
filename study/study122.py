def calculate_tip(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount
    return tip_amount, total_amount

if __name__ == "__main__":
    while True:
        print("\n식사 팁 계산기")
        bill_amount = input("식사 비용을 입력하세요 (종료하려면 '종료'를 입력하세요): ").strip()
        
        if bill_amount.lower() == "종료":
            break

        try:
            bill_amount = float(bill_amount)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        tip_percentage = input("팁 비율을 입력하세요 (예: 15): ").strip()

        try:
            tip_percentage = float(tip_percentage)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        tip_amount, total_amount = calculate_tip(bill_amount, tip_percentage)
        print(f"팁 금액: {tip_amount:.2f}원")
        print(f"총 금액: {total_amount:.2f}원")
