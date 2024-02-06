try:
    # 파일 열기
    with open('numbers.txt', 'r') as file:
        # 파일에서 숫자 읽어오기
        numbers = [int(line.strip()) for line in file]

        # 숫자의 합 계산
        total = sum(numbers)

        # 결과 출력
        print("파일에서 읽어온 숫자:", numbers)
        print("숫자의 합:", total)

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

except ValueError:
    print("파일에 올바른 숫자가 포함되어 있지 않습니다.")