def fibonacci(n):
    """ n개의 피보나치 수열을 생성하는 함수 """
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    print("피보나치 수열 생성기에 오신 것을 환영합니다.")
    n = int(input("생성할 피보나치 수열의 길이를 입력하세요: "))
    if n <= 0:
        print("1 이상의 수를 입력해야 합니다.")
    else:
        sequence = fibonacci(n)
        print(f"피보나치 수열 ({n} 항): {sequence}")

if __name__ == "__main__":
    main()
