from datetime import datetime, timedelta

def calculate_date(days=0, weeks=0, months=0, years=0):
    now = datetime.now()
    delta = timedelta(days=days + weeks * 7)


    months_delta = timedelta(days=months * 30)
    years_delta = timedelta(days=years * 365)

    result_date = now + delta + months_delta + years_delta
    return result_date

def main():
    print("기간을 입력하세요:")
    days = int(input("일: "))
    weeks = int(input("주: "))
    months = int(input("월: "))
    years = int(input("년: "))

    result_date = calculate_date(days, weeks, months, years)
    print(f"계산된 날짜 및 시간: {result_date.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
