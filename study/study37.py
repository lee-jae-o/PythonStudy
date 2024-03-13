def is_prime(num):
    """
    주어진 숫자가 소수인지를 판별하는 함수
    """
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# 테스트
number = int(input("숫자를 입력하세요: "))
if is_prime(number):
    print(number, "는(은) 소수입니다.")
else:
    print(number, "는(은) 소수가 아닙니다.")