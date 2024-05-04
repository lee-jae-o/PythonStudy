def max_food_items(menu, budget):
    affordable_items = []

   
    for item in menu:
        if item['price'] <= budget:
            affordable_items.append(item)

    affordable_items.sort(key=lambda x: x['price'])

    total_items = 0
    remaining_budget = budget

  
    for item in affordable_items:
        if item['price'] <= remaining_budget:
            total_items += 1
            remaining_budget -= item['price']
        else:
            break

    return total_items

if __name__ == "__main__":
    menu = [
        {'name': '스테이크', 'price': 30000},
        {'name': '파스타', 'price': 20000},
        {'name': '피자', 'price': 15000},
        {'name': '샐러드', 'price': 10000},
        {'name': '스프', 'price': 8000}
    ]

    budget = 50000

    max_items = max_food_items(menu, budget)
    print("예산 내에서 최대한 많이 구매할 수 있는 음식의 수:", max_items)