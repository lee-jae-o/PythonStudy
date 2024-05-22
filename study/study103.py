def maximize_dishes(dishes, available_time):
    
    dishes.sort(key=lambda x: x['prep_time'])

    prepared_dishes = []
    total_time = 0

    for dish in dishes:
        if total_time + dish['prep_time'] + dish['cook_time'] <= available_time:
            prepared_dishes.append(dish)
            total_time += dish['prep_time'] + dish['cook_time']

    return prepared_dishes, total_time

if __name__ == "__main__":
    dishes = [
        {'name': 'Spaghetti', 'prep_time': 20, 'cook_time': 30},
        {'name': 'Salad', 'prep_time': 10, 'cook_time': 0},
        {'name': 'Steak', 'prep_time': 15, 'cook_time': 25},
        {'name': 'Soup', 'prep_time': 10, 'cook_time': 15},
        {'name': 'Cake', 'prep_time': 30, 'cook_time': 45}
    ]

    available_time = 60  

    prepared_dishes, total_time = maximize_dishes(dishes, available_time)

    print("준비한 요리들:")
    for dish in prepared_dishes:
        print(f"{dish['name']} - 준비 시간: {dish['prep_time']}분, 요리 시간: {dish['cook_time']}분")
    print(f"총 소요 시간: {total_time}분")