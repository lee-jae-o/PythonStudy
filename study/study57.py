def 중간값_찾기(a, b, c):
    if (b <= a <= c) or (c <= a <= b):
        return a
    elif (a <= b <= c) or (c <= b <= a):
        return b
    else:
        return c

if __name__ == "__main__":
    num1 = int(input("첫 번째 정수를 입력하세요: "))
    num2 = int(input("두 번째 정수를 입력하세요: "))
    num3 = int(input("세 번째 정수를 입력하세요: "))
    
    중간값 = 중간값_찾기(num1, num2, num3)
    print(f"입력한 세 정수 중 중간값은 {중간값}입니다.")