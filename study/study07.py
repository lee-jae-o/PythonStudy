def print_gugudan():
    try:
        # 사용자에게 숫자 입력 받기
        num = int(input("구구단을 출력할 숫자를 입력하세요: "))

        # 입력된 숫자에 해당하는 구구단 출력
        print(f"{num}단:")
        for i in range(1, 10):
            result = num * i
            print(f"{num} x {i} = {result}")

    except ValueError:
        print("올바른 숫자를 입력하세요.")

# 함수 호출
print_gugudan()