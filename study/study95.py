import math

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        sqrt_num = int(math.sqrt(number))
        for i in range(3, sqrt_num + 1, 2):
            if number % i == 0:
                return False
        return True

if __name__ == "__main__":
    num = 17
    if is_prime(num):
        print(f"{num}은(는) 소수입니다.")
    else:
        print(f"{num}은(는) 소수가 아닙니다.")