class FourCal:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

a = FourCal(1, 2)

print(f"첫번째 숫자: {a.first}")
print(f"두번째 숫자: {a.second}")
print(f"더하기 결과: {a.add()}")

print("-----------------")
class MoreForCal(FourCal):
    def square(self):
        result = self.first ** self.second
        return result

a = MoreForCal(3, 3)

print(f"자식 클래스 첫번째 숫자: {a.first}")
print(f"자식 클래스 두번째 숫자: {a.second}")
print(f"자식 클래스 더하기 결과: {a.add()}")
print(f"자식 클래스 새로운 함수 결과: {a.square()}")

