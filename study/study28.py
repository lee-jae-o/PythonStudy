import random

def 간단로또번호생성():
    print("간단한 로또 번호 생성기에 오신 것을 환영합니다!")

    로또번호 = random.sample(range(1, 46), 6)
    보너스번호 = random.randint(1, 45)

    print("로또 번호:", 로또번호)
    print("보너스 번호:", 보너스번호)

if __name__ == "__main__":
    간단로또번호생성()