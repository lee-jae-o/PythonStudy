menu = {
    "에스프레소": 2000,
    "아메리카노": 3000,
    "라떼": 3500,
    "에이드": 4000
}

total_price = 0

while True:
    print("---- 메뉴 ----")
    for item, price in menu.items():
        print(f"{item}: {price}원")

    choice = input("\n주문할 음료를 입력하세요 (종료하려면 'q' 입력): ")

    if choice == "q":
        break

    if choice in menu:
        try:
            quantity = int(input(f"{choice} 몇 잔을 주문하시겠습니까? "))
            if quantity > 0:
                total_price += menu[choice] * quantity
                print(f"{choice} {quantity}잔 추가되었습니다. 현재 총 금액: {total_price}원")
            else:
                print("올바른 수량을 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")
    else:
        print("메뉴에 없는 항목입니다. 다시 입력해주세요.")

print(f"\n최종 결제 금액은 {total_price}원 입니다. 주문이 완료되었습니다!")
