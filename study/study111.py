class Restaurant:
    def __init__(self, tables):
        self.tables = tables  
        self.reservations = {}  

    def make_reservation(self, time_slot, party_size):
        if time_slot not in self.reservations:
            self.reservations[time_slot] = [0] * len(self.tables)

        for i, capacity in enumerate(self.tables):
            if self.reservations[time_slot][i] == 0 and capacity >= party_size:
                self.reservations[time_slot][i] = party_size
                return f"예약이 완료되었습니다. 테이블 번호: {i+1}"

        return "예약 가능한 테이블이 없습니다."

    def check_availability(self, time_slot):
        if time_slot not in self.reservations:
            return self.tables
        return [capacity - reserved if reserved == 0 else 0 for capacity, reserved in zip(self.tables, self.reservations[time_slot])]

if __name__ == "__main__":
    tables = [4, 4, 2, 2, 6] 
    restaurant = Restaurant(tables)

    print(restaurant.make_reservation("18:00", 3))
    print(restaurant.make_reservation("18:00", 2))
    print(restaurant.make_reservation("18:00", 5))
    print(restaurant.make_reservation("18:00", 2))

    print("18:00 시각의 테이블 예약 상태:")
    print(restaurant.check_availability("18:00"))