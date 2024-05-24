def optimize_purchase(items, coupons, budget):
 
    for item in items:
        best_discount = max([coupon for coupon in coupons if coupon <= item['price']], default=0)
        item['discounted_price'] = item['price'] - best_discount

   
    items.sort(key=lambda x: x['discounted_price'])

    purchased_items = []
    total_spent = 0

    for item in items:
        if total_spent + item['discounted_price'] <= budget:
            purchased_items.append(item)
            total_spent += item['discounted_price']

    return purchased_items, total_spent

if __name__ == "__main__":
    items = [
        {'name': 'Notebook', 'price': 500},
        {'name': 'Pen', 'price': 100},
        {'name': 'Pencil', 'price': 50},
        {'name': 'Eraser', 'price': 30},
        {'name': 'Ruler', 'price': 200}
    ]

    coupons = [20, 50, 100]  
    budget = 300

    purchased_items, total_spent = optimize_purchase(items, coupons, budget)

    print("구매한 물품들:")
    for item in purchased_items:
        print(f"{item['name']} - 원래 가격: {item['price']}원, 할인된 가격: {item['discounted_price']}원")
    print(f"총 사용 금액: {total_spent}원, 남은 예산: {budget - total_spent}원")