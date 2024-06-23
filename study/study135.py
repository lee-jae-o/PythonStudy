class ReservationSystem:
    def __init__(self):
        self.reservations = {}

    def reserve_table(self, date, time, name):
        if date not in self.reservations:
            self.reservations[date] = {}
        if time not in self.reservations[date]:
            self.reservations[date][time] = None

        if self.reservations[date][time] is None:
            self.reservations[date][time] = name
            print(f"{name}님, {date} {time}에 예약되었습니다.")
        else:
            print(f"죄송합니다. {date} {time}에 이미 예약이 있습니다.")

    def cancel_reservation(self, date, time, name):
        if date in self.reservations and time in self.reservations[date]:
            if self.reservations[date][time] == name:
                self.reservations[date][time] = None
                print(f"{name}님, {date} {time}의 예약이 취소되었습니다.")
            else:
                print(f"해당 시간에 {name}님의 예약이 없습니다.")
        else:
            print(f"{date} {time}에 예약이 없습니다.")

    def view_reservations(self, date):
        if date in self.reservations:
            print(f"{date}의 예약 목록:")
            for time, name in self.reservations[date].items():
                if name:
                    print(f"{time}: {name}")
                else:
                    print(f"{time}: 예약 없음")
        else:
            print(f"{date}에 예약이 없습니다.")

if __name__ == "__main__":
    system = ReservationSystem()

    while True:
        print("\n1. 예약하기")
        print("\n2. 예약 취소하기")
        print("\n3. 예약 목록 보기")
        print("\n4. 종료하기")
        choice = int(input("원하는 작업을 선택하세요: ").strip())

        if choice == 1:
            date = input("예약 날짜 (YYYY-MM-DD): ").strip()
            time = input("예약 시간 (HH:MM): ").strip()
            name = input("예약자 이름: ").strip()
            system.reserve_table(date, time, name)
        elif choice == 2:
            date = input("예약 취소 날짜 (YYYY-MM-DD): ").strip()
            time = input("예약 취소 시간 (HH:MM): ").strip()
            name = input("예약자 이름: ").strip()
            system.cancel_reservation(date, time, name)
        elif choice == 3:
            date = input("조회할 날짜 (YYYY-MM-DD): ").strip()
            system.view_reservations(date)
        elif choice == 4:
            print("시스템을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
