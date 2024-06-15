def calculate_compound_interest(principal, annual_rate, years, annual_contribution=0):
    total_amount = principal
    for year in range(1, years + 1):
        total_amount += annual_contribution
        total_amount *= (1 + annual_rate / 100)
    return total_amount

if __name__ == "__main__":
    while True:
        print("\n복리 계산기")
        principal = input("초기 투자 금액을 입력하세요 (종료하려면 '종료'를 입력하세요): ").strip()
        
        if principal.lower() == "종료":
            break

        try:
            principal = float(principal)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        annual_rate = input("연간 이율을 입력하세요 (%): ").strip()

        try:
            annual_rate = float(annual_rate)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        years = input("투자 기간(년)을 입력하세요: ").strip()

        try:
            years = int(years)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        annual_contribution = input("연간 추가 투자 금액을 입력하세요 (없으면 0 입력): ").strip()

        try:
            annual_contribution = float(annual_contribution)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        final_amount = calculate_compound_interest(principal, annual_rate, years, annual_contribution)
        print(f"최종 금액: {final_amount:.2f}원")
