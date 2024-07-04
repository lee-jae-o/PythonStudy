def calculate_water_intake(weight_kg):
  
    recommended_intake = weight_kg * 35 
    return recommended_intake

def main():
    print("물 섭취 추천 프로그램에 오신 것을 환영합니다.")
    try:
        weight_kg = float(input("당신의 체중(kg)을 입력하세요: "))
        if weight_kg <= 0:
            print("올바른 체중 값을 입력해 주세요.")
        else:
            water_intake = calculate_water_intake(weight_kg)
            print(f"당신의 하루 권장 물 섭취량은 약 {water_intake}ml입니다.")
    except ValueError:
        print("숫자를 입력해야 합니다. 프로그램을 다시 시작해 주세요.")

if __name__ == "__main__":
    main()
