class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"{item_name}이(가) {quantity}개 추가되었습니다.")

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            print(f"{item_name}이(가) {quantity}개 제거되었습니다.")
            if self.items[item_name] == 0:
                del self.items[item_name]
        else:
            print("재고가 부족하거나 해당 물품이 없습니다.")

    def view_inventory(self):
        if not self.items:
            print("재고가 비어 있습니다.")
        else:
            print("현재 재고 목록:")
            for item_name, quantity in self.items.items():
                print(f"{item_name}: {quantity}개")

if __name__ == "__main__":
    inventory = Inventory()

    while True:
        print("\n1. 물품 추가하기")
        print("2. 물품 제거하기")
        print("3. 재고 목록 보기")
        print("4. 종료하기")
        choice = int(input("원하는 작업을 선택하세요: ").strip())

        if choice == 1:
            item_name = input("물품 이름: ").strip()
            quantity = int(input("물품 수량: ").strip())
            inventory.add_item(item_name, quantity)
        elif choice == 2:
            item_name = input("물품 이름: ").strip()
            quantity = int(input("제거할 수량: ").strip())
            inventory.remove_item(item_name, quantity)
        elif choice == 3:
            inventory.view_inventory()
        elif choice == 4:
            print("시스템을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
