class ShoppingAssistant:
    def __init__(self):
        self.products = {}

    def add_product(self, product_name, store_name, price):
        if product_name not in self.products:
            self.products[product_name] = {}
        self.products[product_name][store_name] = price
        print(f"{store_name}에서 {product_name}이(가) {price}원에 추가되었습니다.")

    def compare_prices(self, product_name):
        if product_name in self.products:
            lowest_price = None
            cheapest_store = None
            print(f"{product_name}의 가격 비교:")
            for store, price in self.products[product_name].items():
                print(f"{store}: {price}원")
                if lowest_price is None or price < lowest_price:
                    lowest_price = price
                    cheapest_store = store
            print(f"가장 저렴한 곳은 {cheapest_store}에서 {lowest_price}원입니다.")
        else:
            print(f"오류: {product_name}에 대한 정보가 없습니다.")

def main():
    assistant = ShoppingAssistant()
    while True:
        print("\n1. 제품 추가")
        print("2. 가격 비교")
        print("3. 종료")
        choice = input("선택하세요: ")

        if choice == '1':
            product_name = input("제품 이름을 입력하세요: ")
            store_name = input("상점 이름을 입력하세요: ")
            price = float(input("가격을 입력하세요: "))
            assistant.add_product(product_name, store_name, price)
        elif choice == '2':
            product_name = input("가격을 비교할 제품 이름을 입력하세요: ")
            assistant.compare_prices(product_name)
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
