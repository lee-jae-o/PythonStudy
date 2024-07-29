def gcd(x, y):
    """ 두 수 x, y의 최대 공약수를 계산하는 함수 """
    while y != 0:
        (x, y) = (y, x % y)
    return x

def lcm(x, y):
    """ 두 수 x, y의 최소 공배수를 계산하는 함수 """
    return abs(x * y) // gcd(x, y)

def main():
    print("최대 공약수와 최소 공배수 계산기에 오신 것을 환영합니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    
    gcd_result = gcd(num1, num2)
    lcm_result = lcm(num1, num2)
    
    print(f"{num1}과(와) {num2}의 최대 공약수는 {gcd_result}입니다.")
    print(f"{num1}과(와) {num2}의 최소 공배수는 {lcm_result}입니다.")

if __name__ == "__main__":
    main()
