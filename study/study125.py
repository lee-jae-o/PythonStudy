def calculate_discounted_price(original_price, discount_rate):
    discount_amount = original_price * (discount_rate / 100)
    discounted_price = original_price - discount_amount
    return discount_amount, discounted_price

if __name__ == "__main__":
    while True:
        print("\n할인 계산기")
        original_price = input("상품의 원래 가격을 입력하세요 (종료하려면 '종료'를 입력하세요): ").strip()
        
        if original_price.lower() == "종료":
            break

        try:
            original_price = float(original_price)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        discount_rate = input("할인율을 입력하세요 (%): ").strip()

        try:
            discount_rate = float(discount_rate)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        discount_amount, discounted_price = calculate_discounted_price(original_price, discount_rate)
        print(f"할인 금액: {discount_amount:.2f}원")
        print(f"할인된 가격: {discounted_price:.2f}원")
