def 계산기(숫자1, 연산자, 숫자2):
    if 연산자 == '+':
        return 숫자1 + 숫자2
    elif 연산자 == '-':
        return 숫자1 - 숫자2
    elif 연산자 == '*':
        return 숫자1 * 숫자2
    elif 연산자 == '/':
        if 숫자2 != 0:
            return 숫자1 / 숫자2
        else:
            return "0으로 나눌 수 없습니다."
    else:
        return "올바르지 않은 연산자입니다."

if __name__ == "__main__":
    숫자1 = float(input("첫 번째 숫자를 입력하세요: "))
    연산자 = input("사칙연산 중 하나를 선택하세요 (+, -, *, /): ")
    숫자2 = float(input("두 번째 숫자를 입력하세요: "))

    결과 = 계산기(숫자1, 연산자, 숫자2)
    print(f"결과: {결과}")