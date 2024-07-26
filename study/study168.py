def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "0으로 나눌 수 없습니다."

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("유효한 숫자를 입력하세요.")

def get_operation_input():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    while True:
        operation = input("수행할 연산을 입력하세요 (+, -, *, /): ")
        if operation in operations:
            return operations[operation]
        else:
            print("지원하지 않는 연산입니다. 다시 입력해 주세요.")

def main():
    print("간단한 CLI 계산기에 오신 것을 환영합니다.")
    while True:
        num1 = get_number_input("첫 번째 숫자를 입력하세요: ")
        num2 = get_number_input("두 번째 숫자를 입력하세요: ")
        operation = get_operation_input()
        result = operation(num1, num2)
        print(f"결과: {result}")
        if input("계산을 계속 하시겠습니까? (y/n): ").lower() != 'y':
            print("계산기를 종료합니다.")
            break

if __name__ == "__main__":
    main()
