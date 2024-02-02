import random

def rock_paper_scissors():
    choices = ['가위', '바위', '보']

    user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
    computer_choice = random.choice(choices)

    print(f"당신의 선택: {user_choice}")
    print(f"컴퓨터의 선택: {computer_choice}")

    if user_choice == computer_choice:
        print("비겼습니다!")
    elif (
        (user_choice == '가위' and computer_choice == '보') or
        (user_choice == '바위' and computer_choice == '가위') or
        (user_choice == '보' and computer_choice == '바위')
    ):
        print("당신이 이겼습니다!")
    else:
        print("컴퓨터가 이겼습니다!")

# 가위 바위 보 게임 실행
rock_paper_scissors()