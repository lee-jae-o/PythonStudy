def calculate_fuel_efficiency(distance, fuel_used):
    if fuel_used <= 0:
        return "연료 사용량은 0보다 커야 합니다."
    fuel_efficiency = distance / fuel_used
    return fuel_efficiency

if __name__ == "__main__":
    while True:
        print("\n연료 효율 계산기")
        distance = input("주행 거리를 입력하세요 (km) (종료하려면 '종료'를 입력하세요): ").strip()

        if distance.lower() == "종료":
            break

        try:
            distance = float(distance)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        fuel_used = input("사용한 연료량을 입력하세요 (L): ").strip()

        try:
            fuel_used = float(fuel_used)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        efficiency = calculate_fuel_efficiency(distance, fuel_used)
        if isinstance(efficiency, str):
            print(efficiency)
        else:
            print(f"연료 효율: {efficiency:.2f} km/L")
