def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("온도 변환기에 오신 것을 환영합니다.")
    mode = input("변환하고 싶은 모드를 선택하세요 (CtoF: 섭씨에서 화씨, FtoC: 화씨에서 섭씨): ")

    if mode == "CtoF":
        celsius = float(input("섭씨 온도를 입력하세요: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C는 {fahrenheit}°F입니다.")
    elif mode == "FtoC":
        fahrenheit = float(input("화씨 온도를 입력하세요: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F는 {celsius}°C입니다.")
    else:
        print("잘못된 모드 선택입니다. CtoF 또는 FtoC를 입력해주세요.")

if __name__ == "__main__":
    main()
