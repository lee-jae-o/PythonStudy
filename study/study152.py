import random

def suggest_meal(meal_type):
    meals = {
        '아침': ['토스트와 계란', '그릭 요거트와 과일', '오트밀과 견과류'],
        '점심': ['샌드위치', '초밥 세트', '닭가슴살 샐러드'],
        '저녁': ['스테이크와 야채', '토마토 파스타', '불고기와 밥']
    }
    
    if meal_type in meals:
        return random.choice(meals[meal_type])
    else:
        return "제공하는 식사 시간대가 아닙니다."

def main():
    print("식사 메뉴 결정기에 오신 것을 환영합니다.")
    meal_type = input("어떤 식사를 하고 싶으신가요? 아침, 점심, 저녁 중 하나를 입력해주세요: ")
    
    suggestion = suggest_meal(meal_type)
    if suggestion != "제공하는 식사 시간대가 아닙니다.":
        print(f"오늘의 {meal_type} 추천 메뉴는 '{suggestion}'입니다.")
    else:
        print(suggestion)

if __name__ == "__main__":
    main()
