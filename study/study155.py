class ParkingLot:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.available_spaces = total_spaces
        self.parked_cars = {}

    def park_car(self, car_id):
        if self.available_spaces > 0:
            if car_id not in self.parked_cars:
                self.parked_cars[car_id] = True
                self.available_spaces -= 1
                print(f"차량 {car_id} 주차 완료. 남은 주차 공간: {self.available_spaces}개")
            else:
                print(f"차량 {car_id}는 이미 주차되어 있습니다.")
        else:
            print("주차 공간이 부족합니다.")

    def leave_parking(self, car_id):
        if car_id in self.parked_cars:
            del self.parked_cars[car_id]
            self.available_spaces += 1
            print(f"차량 {car_id} 출차 완료. 남은 주차 공간: {self.available_spaces}개")
        else:
            print(f"차량 {car_id}는 주차되어 있지 않습니다.")

    def check_available_spaces(self):
        print(f"현재 사용 가능한 주차 공간: {self.available_spaces}개")

def main():
    parking_lot = ParkingLot(50)  

    while True:
        print("\n1. 차량 주차하기")
        print("2. 차량 출차하기")
        print("3. 사용 가능한 주차 공간 확인")
        print("4. 종료하기")
        choice = input("원하는 작업을 선택하세요: ").strip()

        if choice == '1':
            car_id = input("주차할 차량의 번호를 입력하세요: ").strip()
            parking_lot.park_car(car_id)
        elif choice == '2':
            car_id = input("출차할 차량의 번호를 입력하세요: ").strip()
            parking_lot.leave_parking(car_id)
        elif choice == '3':
            parking_lot.check_available_spaces()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
