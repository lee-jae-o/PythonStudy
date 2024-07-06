def convert_seconds_to_time(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return days, hours, minutes, seconds

def main():
    print("시간 변환기에 오신 것을 환영합니다.")
    try:
        total_seconds = int(input("초(second) 단위로 시간을 입력하세요: "))
        if total_seconds < 0:
            print("음수 시간을 입력할 수 없습니다. 양수를 입력해 주세요.")
        else:
            days, hours, minutes, seconds = convert_seconds_to_time(total_seconds)
            print(f"입력하신 시간: {total_seconds}초")
            print(f"변환된 시간: {days}일 {hours}시간 {minutes}분 {seconds}초")
    except ValueError:
        print("숫자를 입력해야 합니다. 프로그램을 다시 시작해 주세요.")

if __name__ == "__main__":
    main()
