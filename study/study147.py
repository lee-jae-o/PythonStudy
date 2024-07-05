def calculate_bmi(weight_kg, height_cm):

    height_m = height_cm / 100

    bmi = weight_kg / (height_m ** 2)
    return bmi

def evaluate_bmi(bmi):
    if bmi < 18.5:
        return "저체중"
    elif 18.5 <= bmi < 25:
        return "정상 체중"
    elif 25 <= bmi < 30:
        return "과체중"
    else:
        return "비만"

def main():
    print("BMI 계산기에 오신 것을 환영합니다.")
    try:
        weight_kg = float(input("당신의 체중(kg)을 입력하세요: "))
        height_cm = float(input("당신의 키(cm)를 입력하세요: "))
        if weight_kg <= 0 or height_cm <= 0:
            print("올바른 체중과 키 값을 입력해 주세요.")
        else:
            bmi = calculate_bmi(weight_kg, height_cm)
            health_status = evaluate_bmi(bmi)
            print(f"당신의 BMI는 {bmi:.2f}이며, 이는 '{health_status}' 범주에 속합니다.")
    except ValueError:
        print("숫자를 입력해야 합니다. 프로그램을 다시 시작해 주세요.")

if __name__ == "__main__":
    main()
