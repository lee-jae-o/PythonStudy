def maximize_value(items, budget):

    items.sort(key=lambda x: x['value'] / x['price'], reverse=True)

    total_value = 0
    purchased_items = []
    remaining_budget = budget

    for item in items:
        if item['price'] <= remaining_budget:
            purchased_items.append(item)
            total_value += item['value']
            remaining_budget -= item['price']
        else:
            break

    return purchased_items, total_value

if __name__ == "__main__":
    items = [
        {'name': 'Notebook', 'price': 500, 'value': 300},
        {'name': 'Pen', 'price': 100, 'value': 70},
        {'name': 'Pencil', 'price': 50, 'value': 30},
        {'name': 'Eraser', 'price': 30, 'value': 20},
        {'name': 'Ruler', 'price': 200, 'value': 150}
    ]

    budget = 300

    purchased_items, total_value = maximize_value(items, budget)
    print("구매한 물품들:")
    for item in purchased_items:
        print(f"{item['name']}: {item['price']}원, 가치: {item['value']}")
    print(f"총 가치: {total_value}")