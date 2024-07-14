import random

def get_motivational_quote():
    quotes = [
        "위대한 일을 하기 위한 유일한 방법은 자신이 하는 일을 사랑하는 것입니다. – 스티브 잡스",
        "끝날 때까지는 항상 불가능해 보입니다. – 넬슨 만델라",
        "시도조차 하지 않은 샷은 100% 놓치게 됩니다. – 웨인 그레츠키",
        "성공이 영원한 것은 아니며, 실패가 치명적인 것도 아닙니다: 중요한 것은 계속될 용기입니다. – 윈스턴 처칠",
        "당신이 할 수 있다고 믿으면, 이미 절반은 성공한 것입니다. – 시어도어 루스벨트"
    ]
    return random.choice(quotes)

def main():
    print("오늘의 동기 부여 명언:")
    quote = get_motivational_quote()
    print(quote)

if __name__ == "__main__":
    main()
