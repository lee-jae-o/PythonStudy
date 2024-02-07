import random

def guess_the_number():
    # 1에서 100 사이의 랜덤 숫자 생성
    secret_number = random.randint(1, 100)

    print("1에서 100 사이의 숫자를 맞춰보세요!")

    while True:
        try:
            # 사용자로부터 숫자 입력 받기
            guess = int(input("추측한 숫자를 입력하세요: "))

            # 숫자 비교
            if guess == secret_number:
                print("축하합니다! 숫자를 맞췄습니다!")
                break
            elif guess < secret_number:
                print("좀 더 큰 수를 입력하세요.")
            else:
                print("좀 더 작은 수를 입력하세요.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

if __name__ == "__main__":
    guess_the_number()