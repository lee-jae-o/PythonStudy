def should_bring_umbrella(weather):
    if weather.lower() in ['비', '소나기', '폭우', '진눈깨비', '눈']:
        return True
    else:
        return False

def main():
    print("우산 가져갈지 말지 결정하는 프로그램에 오신 것을 환영합니다.")
    weather = input("현재 날씨를 입력하세요 (예: 맑음, 흐림, 비, 눈 등): ")
    
    if should_bring_umbrella(weather):
        print("우산을 가져가세요. 날씨가 좋지 않습니다.")
    else:
        print("우산을 가져갈 필요가 없습니다. 날씨가 좋아 보입니다.")

if __name__ == "__main__":
    main()
