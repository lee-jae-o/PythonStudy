def can_purchase_items(items, budget):
    affordable_items = []

    # 주어진 금액으로 살 수 있는 모든 물건을 찾음
    for item in items:
        if item['price'] <= budget:
            affordable_items.append(item)

    # 물건들을 가격순으로 정렬
    affordable_items.sort(key=lambda x: x['price'])

    purchased_items = []
    remaining_budget = budget

    # 최대한 많은 물건을 선택하여 구매
    for item in affordable_items:
        if item['price'] <= remaining_budget:
            purchased_items.append(item)
            remaining_budget -= item['price']
        else:
            break

    return purchased_items

if __name__ == "__main__":
    items = [
        {'name': 'Notebook', 'price': 500},
        {'name': 'Pen', 'price': 100},
        {'name': 'Pencil', 'price': 50},
        {'name': 'Eraser', 'price': 30},
        {'name': 'Ruler', 'price': 200}
    ]

    budget = 300

    affordable_items = can_purchase_items(items, budget)
    print("주어진 금액으로 살 수 있는 물건들:")
    for item in affordable_items:
        print(f"{item['name']}: {item['price']}원")