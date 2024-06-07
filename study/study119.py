import heapq

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        status = "완료" if self.completed else "미완료"
        return f"[{status}] {self.description} (우선순위: {self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        heapq.heappush(self.tasks, task)
        return f"'{description}' 작업이 추가되었습니다. (우선순위: {priority})"

    def complete_task(self, description):
        for task in self.tasks:
            if task.description == description and not task.completed:
                task.completed = True
                return f"'{description}' 작업이 완료되었습니다."
        return f"'{description}' 작업을 찾을 수 없습니다."

    def delete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                heapq.heapify(self.tasks)
                return f"'{description}' 작업이 삭제되었습니다."
        return f"'{description}' 작업을 찾을 수 없습니다."

    def view_tasks(self):
        if not self.tasks:
            return "할 일 목록이 비어 있습니다."
        
        return "현재 할 일 목록:\n" + "\n".join([str(task) for task in sorted(self.tasks)])

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\n무슨 작업을 하시겠습니까? (추가, 완료, 삭제, 보기, 종료): ")
        action = input().strip()

        if action == "종료":
            break

        if action == "추가":
            description = input("작업 내용을 입력하세요: ").strip()
            priority = int(input("우선순위를 입력하세요 (숫자가 낮을수록 우선순위가 높음): ").strip())
            print(task_manager.add_task(description, priority))
        elif action == "완료":
            description = input("완료할 작업 내용을 입력하세요: ").strip()
            print(task_manager.complete_task(description))
        elif action == "삭제":
            description = input("삭제할 작업 내용을 입력하세요: ").strip()
            print(task_manager.delete_task(description))
        elif action == "보기":
            print(task_manager.view_tasks())
        else:
            print("잘못된 작업입니다. '추가', '완료', '삭제', '보기' 또는 '종료'를 입력하세요.")
