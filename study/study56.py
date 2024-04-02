from collections import Counter

def 순열_판별(문자열1, 문자열2):
    카운터1 = Counter(문자열1)
    카운터2 = Counter(문자열2)
    
    return 카운터1 == 카운터2

if __name__ == "__main__":
    문자열1 = input("첫 번째 문자열을 입력하세요: ")
    문자열2 = input("두 번째 문자열을 입력하세요: ")
    
    if 순열_판별(문자열1, 문자열2):
        print("입력한 두 문자열은 서로 순열 관계입니다.")
    else:
        print("입력한 두 문자열은 서로 순열 관계가 아닙니다.")