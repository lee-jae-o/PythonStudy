from datetime import datetime

def 현재날짜와시간출력():
    현재시간 = datetime.now()
    포맷된시간 = 현재시간.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")

    print(f"현재 날짜와 시간: {포맷된시간}")

if __name__ == "__main__":
    현재날짜와시간출력()