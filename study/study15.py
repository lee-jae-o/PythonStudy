def calculator():
    while True:
        # 사용자에게 수식 입력 받기
        expression = input("계산할 수식을 입력하세요 (종료: 'exit'): ")

        # 'exit'을 입력하면 프로그램 종료
        if expression.lower() == 'exit':
            print("계산기를 종료합니다.")
            break

        try:
            # 수식 계산
            result = eval(expression)
            print("결과:", result)
        except (SyntaxError, ZeroDivisionError):
            print("올바른 수식이 아닙니다. 다시 시도하세요.")

if __name__ == "__main__":
    calculator()