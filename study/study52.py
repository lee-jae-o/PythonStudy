def 약수_출력(정수):
    약수들 = []
    for i in range(1, 정수 + 1):
        if 정수 % i == 0:
            약수들.append(i)
    return 약수들

if __name__ == "__main__":
    입력값 = int(input("정수를 입력하세요: "))
    
    if 입력값 <= 0:
        print("양의 정수를 입력해주세요.")
    else:
        결과 = 약수_출력(입력값)
        print(f"{입력값}의 약수는 {결과}입니다.")