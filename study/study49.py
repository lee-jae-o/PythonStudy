def 팩토리얼(n):
    if n == 0:
        return 1
    else:
        return n * 팩토리얼(n - 1)

if __name__ == "__main__":
    입력값 = int(input("정수를 입력하세요: "))
    
    if 입력값 < 0:
        print("음수의 팩토리얼은 정의되지 않습니다.")
    else:
        결과 = 팩토리얼(입력값)
        print(f"{입력값}의 팩토리얼은 {결과}입니다.")