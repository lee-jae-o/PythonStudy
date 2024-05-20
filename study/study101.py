def maximize_savings(items, coupons, budget):
  
    items.sort(key=lambda x: min([x['price'] - coupon for coupon in coupons if x['price'] - coupon > 0], default=x['price']))

    purchased_items = []
    remaining_budget = budget

    for item in items:
    
        applicable_coupons = [coupon for coupon in coupons if item['price'] - coupon <= remaining_budget]
        if applicable_coupons:
            best_coupon = max(applicable_coupons)
            discounted_price = item['price'] - best_coupon
        else:
            discounted_price = item['price']

        if discounted_price <= remaining_budget:
            purchased_items.append({'name': item['name'], 'original_price': item['price'], 'discounted_price': discounted_price})
            remaining_budget -= discounted_price

    return purchased_items, remaining_budget

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

    purchased_items, remaining_budget = maximize_savings(items, coupons, budget)

    print("구매한 물품들:")
    for item in purchased_items:
        print(f"{item['name']}: 원래 가격 {item['original_price']}원, 할인된 가격 {item['discounted_price']}원")
    print(f"남은 예산: {remaining_budget}원")