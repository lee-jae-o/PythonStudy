def maximize_shopping_list(items, budget):
 
    items.sort(key=lambda x: x['price'])

    purchased_items = []
    total_spent = 0

    for item in items:
        if total_spent + item['price'] <= budget:
            purchased_items.append(item)
            total_spent += item['price']
        else:
            break

    return purchased_items, total_spent

if __name__ == "__main__":
    items = [
        {'name': 'Milk', 'price': 2.50},
        {'name': 'Bread', 'price': 1.20},
        {'name': 'Butter', 'price': 3.00},
        {'name': 'Eggs', 'price': 2.00},
        {'name': 'Cheese', 'price': 5.00},
        {'name': 'Apple', 'price': 0.80},
        {'name': 'Banana', 'price': 1.10},
        {'name': 'Chicken', 'price': 7.50}
    ]

    budget = 10.00

    purchased_items, total_spent = maximize_shopping_list(items, budget)

    print("구매한 품목들:")
    for item in purchased_items:
        print(f"{item['name']} - 가격: ${item['price']:.2f}")
    print(f"총 사용 금액: ${total_spent:.2f}")
    print(f"남은 예산: ${budget - total_spent:.2f}")