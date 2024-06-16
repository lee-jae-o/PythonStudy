class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"{item_name}을(를) 장바구니에 추가했습니다.")

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name] > quantity:
                self.items[item_name] -= quantity
                print(f"{item_name}을(를) {quantity}개 삭제했습니다.")
            else:
                del self.items[item_name]
                print(f"{item_name}을(를) 모두 삭제했습니다.")
        else:
            print(f"장바구니에 {item_name}이(가) 없습니다.")

    def view_cart(self):
        if not self.items:
            print("장바구니가 비어 있습니다.")
        else:
            print("장바구니 내역:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}개")

if __name__ == "__main__":
    cart = ShoppingCart()

    while True:
        print("\n전자상거래 장바구니 관리 시스템")
        print("1. 상품 추가")
        print("2. 상품 삭제")
        print("3. 장바구니 조회")
        print("4. 종료")

        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            item_name = input("추가할 상품명을 입력하세요: ").strip()
            quantity = input("수량을 입력하세요 (없으면 1 입력): ").strip()
            try:
                quantity = int(quantity) if quantity else 1
                cart.add_item(item_name, quantity)
            except ValueError:
                print("잘못된 입력입니다. 수량에는 숫자를 입력하세요.")

        elif choice == "2":
            item_name = input("삭제할 상품명을 입력하세요: ").strip()
            quantity = input("삭제할 수량을 입력하세요 (없으면 1 입력): ").strip()
            try:
                quantity = int(quantity) if quantity else 1
                cart.remove_item(item_name, quantity)
            except ValueError:
                print("잘못된 입력입니다. 수량에는 숫자를 입력하세요.")

        elif choice == "3":
            cart.view_cart()

        elif choice == "4":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 메뉴를 다시 선택하세요.")
