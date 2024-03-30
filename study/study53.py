def 소수_판별(숫자):
    if 숫자 <= 1:
        return False
    for i in range(2, int(숫자**0.5) + 1):
        if 숫자 % i == 0:
            return False
    return True

if __name__ == "__main__":
    입력값 = int(input("정수를 입력하세요: "))
    
    if 소수_판별(입력값):
        print(f"{입력값}은(는) 소수입니다.")
    else:
        print(f"{입력값}은(는) 소수가 아닙니다.")