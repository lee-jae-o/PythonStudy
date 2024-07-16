def create_meal_plan(day_meals):
    days_of_the_week = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    meal_plan = {day: meal for day, meal in zip(days_of_the_week, day_meals)}
    return meal_plan

def display_meal_plan(meal_plan):
    print("한 주 동안의 식단 계획:")
    for day, meal in meal_plan.items():
        print(f"{day}: {meal}")

def main():
    print("식사 계획기에 오신 것을 환영합니다. 일주일간의 식단을 입력해 주세요.")
    day_meals = []
    for i in range(7):
        meal = input(f"{i + 1}일째 식단을 입력하세요: ")
        day_meals.append(meal)
    
    meal_plan = create_meal_plan(day_meals)
    display_meal_plan(meal_plan)

if __name__ == "__main__":
    main()
