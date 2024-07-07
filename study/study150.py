import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("숫자 맞추기 게임에 오신 것을 환영합니다!")
    print("1부터 100까지의 숫자 중에서 하나를 맞춰보세요.")

    while True:
        try:
            user_guess = int(input("숫자를 입력하세요: "))
            attempts += 1
            if user_guess < number_to_guess:
                print("너무 낮습니다. 다시 시도하세요.")
            elif user_guess > number_to_guess:
                print("너무 높습니다. 다시 시도하세요.")
            else:
                print(f"축하합니다! 정답은 {number_to_guess}였습니다. 당신은 {attempts}번 만에 맞췄습니다.")
                break
        except ValueError:
            print("유효한 숫자를 입력하세요.")

def main():
    guess_number_game()
    while True:
        play_again = input("다시 플레이하시겠습니까? (yes/no): ")
        if play_again.lower() == 'yes':
            guess_number_game()
        elif play_again.lower() == 'no':
            print("게임을 종료합니다. 감사합니다!")
            break
        else:
            print("yes 또는 no로 답해주세요.")

if __name__ == "__main__":
    main()
