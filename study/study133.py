def fibonacci(n):
    if n <= 0:
        return "N은 1 이상의 정수여야 합니다."
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    n = int(input("N번째 피보나치 수를 구하기 위해 N을 입력하세요: ").strip())

    if n <= 0:
        print("N은 1 이상의 정수여야 합니다.")
    else:
        result = fibonacci(n)
        print(f"N번째 피보나치 수는 {result}입니다.")
