def optimize_shopping_list(stores, budget):
    all_items = []
    
   
    for store in stores:
        all_items.extend(store['items'])

   
    all_items.sort(key=lambda x: x['price'])

    purchased_items = []
    total_cost = 0

    for item in all_items:
        if total_cost + item['price'] <= budget:
            purchased_items.append(item)
            total_cost += item['price']

    return purchased_items, total_cost

if __name__ == "__main__":
    stores = [
        {'name': 'Store A', 'items': [{'name': 'Milk', 'price': 50}, {'name': 'Bread', 'price': 20}]},
        {'name': 'Store B', 'items': [{'name': 'Milk', 'price': 40}, {'name': 'Bread', 'price': 25}, {'name': 'Eggs', 'price': 30}]},
        {'name': 'Store C', 'items': [{'name': 'Eggs', 'price': 35}, {'name': 'Butter', 'price': 80}]}
    ]

    budget = 100  

    purchased_items, total_cost = optimize_shopping_list(stores, budget)

    print("구매한 물건들:")
    for item in purchased_items:
        print(f"{item['name']} - 가격: {item['price']}원")
    print(f"총 비용: {total_cost}원")