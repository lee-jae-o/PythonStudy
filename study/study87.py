def calculate_monthly_expenses(daily_expenses):
    total_expenses = sum(daily_expenses)
    return total_expenses

if __name__ == "__main__":
    daily_expenses = [10000, 20000, 15000, 30000, 25000, 20000, 18000, 22000, 25000, 28000, 30000, 35000]
    
    monthly_expenses = calculate_monthly_expenses(daily_expenses)
    print("한 달 동안의 총 지출 금액:", monthly_expenses)