class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return f"'{item}' 아이템이 추가되었습니다."

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return f"'{item}' 아이템이 제거되었습니다."
        else:
            return f"'{item}' 아이템이 목록에 없습니다."

    def view_items(self):
        if self.items:
            return "현재 쇼핑 목록:\n" + "\n".join(self.items)
        else:
            return "쇼핑 목록이 비어 있습니다."

if __name__ == "__main__":
    shopping_list = ShoppingList()

    while True:
        action = input("\n무슨 작업을 하시겠습니까? (추가, 제거, 보기, 종료): ").strip()

        if action == "종료":
            break

        if action == "추가":
            item = input("추가할 아이템을 입력하세요: ").strip()
            print(shopping_list.add_item(item))
        elif action == "제거":
            item = input("제거할 아이템을 입력하세요: ").strip()
            print(shopping_list.remove_item(item))
        elif action == "보기":
            print(shopping_list.view_items())
        else:
            print("잘못된 작업입니다. '추가', '제거', '보기' 또는 '종료'를 입력하세요.")