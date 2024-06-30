import os
import json

class ScheduleManager:
    def __init__(self, filename):
        self.filename = filename
        self.schedules = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.schedules = json.load(file)

    def add_schedule(self, schedule):
        self.schedules.append(schedule)
        self.save()
        print(f"일정 '{schedule}'이(가) 추가되었습니다.")

    def remove_schedule(self, schedule):
        if schedule in self.schedules:
            self.schedules.remove(schedule)
            self.save()
            print(f"일정 '{schedule}'이(가) 삭제되었습니다.")
        else:
            print("해당 일정이 존재하지 않습니다.")

    def view_schedules(self):
        if self.schedules:
            print("현재 일정:")
            for idx, schedule in enumerate(self.schedules, start=1):
                print(f"{idx}. {schedule}")
        else:
            print("저장된 일정이 없습니다.")

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.schedules, file)

def main():
    manager = ScheduleManager('schedules.json')

    while True:
        print("\n개인 일정 관리 프로그램")
        print("1. 일정 추가")
        print("2. 일정 삭제")
        print("3. 일정 확인")
        print("4. 종료")
        choice = input("선택: ").strip()

        if choice == '1':
            schedule = input("추가할 일정을 입력하세요: ")
            manager.add_schedule(schedule)
        elif choice == '2':
            schedule = input("삭제할 일정을 입력하세요: ")
            manager.remove_schedule(schedule)
        elif choice == '3':
            manager.view_schedules()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
