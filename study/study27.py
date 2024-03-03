import random

def 랜덤단어맞추기():
    단어목록 = ["사과", "바나나", "딸기", "포도", "수박", "키위"]
    랜덤단어 = random.choice(단어목록)
    추측단어 = "_" * len(랜덤단어)
    
    print("랜덤 단어 맞추기 게임에 오신 것을 환영합니다!")
    print(f"현재 단어: {추측단어}")

    while "_" in 추측단어:
        사용자입력 = input("한 글자를 추측하세요: ")
        
        if len(사용자입력) == 1 and 사용자입력.isalpha():
            정답여부 = False

            for index, 글자 in enumerate(랜덤단어):
                if 글자 == 사용자입력:
                    추측단어 = 추측단어[:index] + 사용자입력 + 추측단어[index+1:]
                    정답여부 = True

            if 정답여부:
                print(f"정답입니다! 현재 단어: {추측단어}")
            else:
                print("틀렸어요! 다시 시도해보세요.")
        else:
            print("올바른 형식으로 입력하세요.")

    print(f"축하합니다! 정답을 맞추셨습니다. 단어는 '{랜덤단어}'입니다.")

if __name__ == "__main__":
    랜덤단어맞추기()