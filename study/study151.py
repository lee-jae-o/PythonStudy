from datetime import datetime

def calculate_days_between_dates(date1, date2):
    date_format = "%Y-%m-%d"
    try:
        d1 = datetime.strptime(date1, date_format)
        d2 = datetime.strptime(date2, date_format)
        delta = abs((d2 - d1).days)
        return delta
    except ValueError:
        return "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 입력해주세요."

def main():
    print("두 날짜 간의 날짜 수를 계산합니다.")
    date1 = input("첫 번째 날짜를 YYYY-MM-DD 형식으로 입력하세요: ")
    date2 = input("두 번째 날짜를 YYYY-MM-DD 형식으로 입력하세요: ")

    result = calculate_days_between_dates(date1, date2)
    if isinstance(result, int):
        print(f"두 날짜 사이의 일수는 {result}일입니다.")
    else:
        print(result)

if __name__ == "__main__":
    main()
