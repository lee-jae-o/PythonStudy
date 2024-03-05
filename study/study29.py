def 간단BMICalculator():
    print("간단한 BMI 계산기에 오신 것을 환영합니다!")
    키 = float(input("키를 미터 단위로 입력하세요: "))
    몸무게 = float(input("몸무게를 킬로그램 단위로 입력하세요: "))

    bmi = 몸무게 / (키 ** 2)

    print(f"당신의 BMI는 {bmi:.2f}입니다.")

    if bmi < 18.5:
        print("저체중입니다.")
    elif 18.5 <= bmi < 25:
        print("정상체중입니다.")
    elif 25 <= bmi < 30:
        print("과체중입니다.")
    else:
        print("비만입니다.")

if __name__ == "__main__":
    간단BMICalculator()