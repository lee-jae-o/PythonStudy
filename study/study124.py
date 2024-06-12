def calculate_months_to_goal(goal_amount, current_savings, monthly_savings):
    if monthly_savings <= 0:
        return "월 저축 금액은 0보다 커야 합니다."
    remaining_amount = goal_amount - current_savings
    if remaining_amount <= 0:
        return "이미 목표 금액을 달성하였습니다."
    months_needed = remaining_amount / monthly_savings
    return months_needed

if __name__ == "__main__":
    while True:
        print("\n저축 목표 계산기")
        goal_amount = input("저축 목표 금액을 입력하세요 (종료하려면 '종료'를 입력하세요): ").strip()

        if goal_amount.lower() == "종료":
            break

        try:
            goal_amount = float(goal_amount)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        current_savings = input("현재 저축 금액을 입력하세요: ").strip()

        try:
            current_savings = float(current_savings)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        monthly_savings = input("월 저축 금액을 입력하세요: ").strip()

        try:
            monthly_savings = float(monthly_savings)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        months_needed = calculate_months_to_goal(goal_amount, current_savings, monthly_savings)
        if isinstance(months_needed, str):
            print(months_needed)
        else:
            print(f"목표 금액에 도달하기까지 필요한 시간: {months_needed:.1f}개월")
