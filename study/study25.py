def 할일목록관리():
    할일목록 = []

    while True:
        print("\n할 일 목록:")
        for index, 할일 in enumerate(할일목록, start=1):
            print(f"{index}. {할일}")

        print("\n할 일을 선택하세요:")
        print("1. 할 일 추가")
        print("2. 할 일 삭제")
        print("3. 종료")

        선택 = input("선택: ")

        if 선택 == "1":
            새할일 = input("추가할 할 일을 입력하세요: ")
            할일목록.append(새할일)
            print(f"{새할일}이(가) 할 일 목록에 추가되었습니다.")
        elif 선택 == "2":
            if not 할일목록:
                print("삭제할 할 일이 없습니다.")
            else:
                삭제인덱스 = int(input("삭제할 할 일의 번호를 입력하세요: "))
                if 1 <= 삭제인덱스 <= len(할일목록):
                    삭제된할일 = 할일목록.pop(삭제인덱스 - 1)
                    print(f"{삭제된할일}이(가) 할 일 목록에서 삭제되었습니다.")
                else:
                    print("올바른 번호를 입력하세요.")
        elif 선택 == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택을 입력하세요.")

if __name__ == "__main__":
    할일목록관리()