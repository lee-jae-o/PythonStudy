def 소수_판별(숫자):
    if 숫자 < 2:
        return False
    for i in range(2, int(숫자 ** 0.5) + 1):
        if 숫자 % i == 0:
            return False
    return True

def 소수_범위_출력(시작, 끝):
    print(f"{시작}부터 {끝}까지의 소수:")
    for 숫자 in range(시작, 끝 + 1):
        if 소수_판별(숫자):
            print(숫자, end=" ")

if __name__ == "__main__":
    시작 = int(input("시작 숫자를 입력하세요: "))
    끝 = int(input("끝 숫자를 입력하세요: "))

    소수_범위_출력(시작, 끝)