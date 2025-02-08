import time
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # 0 ~ 100 (낮을수록 배부름)
        self.happiness = 50  # 0 ~ 100 (높을수록 행복)

    def feed(self):
        self.hunger = max(0, self.hunger - random.randint(10, 30))
        print(f"{self.name}에게 밥을 줬어요! 🍖 현재 배고픔: {self.hunger}")

    def play(self):
        self.happiness = min(100, self.happiness + random.randint(10, 30))
        print(f"{self.name}와 놀아줬어요! 🎾 현재 행복도: {self.happiness}")

    def status(self):
        print(f"\n📌 {self.name}의 상태")
        print(f"🍽 배고픔: {self.hunger}/100")
        print(f"😄 행복도: {self.happiness}/100\n")

    def time_passes(self):
        self.hunger = min(100, self.hunger + 5)
        self.happiness = max(0, self.happiness - 5)

        if self.hunger >= 80:
            print(f"⚠️ {self.name}가 배고파해요!")
        if self.happiness <= 20:
            print(f"⚠️ {self.name}가 심심해하고 있어요!")

def main():
    pet_name = input("가상 애완동물의 이름을 정해주세요: ")
    pet = VirtualPet(pet_name)

    while True:
        pet.status()
        print("1. 밥 주기 🍖")
        print("2. 놀아주기 🎾")
        print("3. 나가기 🚪")
        choice = input("무엇을 할까요? (1/2/3): ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            print(f"👋 {pet.name}와(과) 작별 인사를 했어요. 안녕~!")
            break
        else:
            print("❌ 잘못된 입력입니다. 다시 선택해주세요.")

        pet.time_passes()
        time.sleep(1)

if __name__ == "__main__":
    main()
