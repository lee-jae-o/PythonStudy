class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, quantity):
        self.items.append({"name": item_name, "quantity": quantity})
        print(f"{item_name}이(가) {quantity}개 추가되었습니다.")

    def remove_item(self, item_name):
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)
                print(f"{item_name}이(가) 목록에서 삭제되었습니다.")
                return
        print("해당 물건이 목록에 없습니다.")

    def view_items(self):
        if not self.items:
            print("쇼핑 목록이 비어 있습니다.")
        else:
            print("쇼핑 목록:")
            for item in self.items:
                print(f"{item['name']}: {item['quantity']}개")

if __name__ == "__main__":
    shopping_list = ShoppingList()

    while True:
        print("\n1. 물건 추가하기")
        print("2. 물건 삭제하기")
        print("3. 쇼핑 목록 보기")
        print("4. 종료하기")
        choice = int(input("원하는 작업을 선택하세요: ").strip())

        if choice == 1:
            item_name = input("물건 이름: ").strip()
            quantity = int(input("수량: ").strip())
            shopping_list.add_item(item_name, quantity)
        elif choice == 2:
            item_name = input("삭제할 물건 이름: ").strip()
            shopping_list.remove_item(item_name)
        elif choice == 3:
            shopping_list.view_items()
        elif choice == 4:
            print("시스템을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
