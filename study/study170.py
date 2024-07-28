def is_prime(n):
    """ 주어진 숫자 n이 소수인지 판별하는 함수 """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    print("소수 판별 프로그램에 오신 것을 환영합니다.")
    number = int(input("소수인지 판별할 숫자를 입력하세요: "))
    if is_prime(number):
        print(f"{number}은(는) 소수입니다.")
    else:
        print(f"{number}은(는) 소수가 아닙니다.")

if __name__ == "__main__":
    main()
