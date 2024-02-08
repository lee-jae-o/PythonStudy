class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"할 일 '{task}'이(가) 추가되었습니다.")

    def view_tasks(self):
        if not self.tasks:
            print("할 일이 없습니다.")
        else:
            print("할 일 목록:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

# To-Do 리스트 객체 생성
todo_list = ToDoList()

while True:
    # 사용자에게 명령어 입력 받기
    command = input("명령어를 입력하세요 (추가: add, 조회: view, 종료: exit): ").lower()

    if command == 'add':
        task = input("추가할 할 일을 입력하세요: ")
        todo_list.add_task(task)
    elif command == 'view':
        todo_list.view_tasks()
    elif command == 'exit':
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 명령어를 입력하세요.")