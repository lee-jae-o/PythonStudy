import random

def 숫자맞추기게임():
    비밀숫자 = random.randint(1, 100)
    시도횟수 = 0

    print("숫자 맞추기 게임에 오신 것을 환영합니다!")
    print("1부터 100 사이의 숫자 중 하나를 선택했습니다. 맞춰보세요.")

    while True:
        사용자입력 = int(input("추측한 숫자를 입력하세요: "))
        시도횟수 += 1

        if 사용자입력 == 비밀숫자:
            print(f"축하합니다! {비밀숫자} 숫자를 {시도횟수}번의 시도 끝에 맞추셨습니다.")
            break
        elif 사용자입력 < 비밀숫자:
            print("너무 낮아요! 다시 시도해보세요.")
        else:
            print("너무 높아요! 다시 시도해보세요.")

if __name__ == "__main__":
    숫자맞추기게임()