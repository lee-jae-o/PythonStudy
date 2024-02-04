numbers = []
num_count = int(input("입력할 숫자의 개수를 입력하세요: "))

for i in range(num_count):
    num = float(input(f"{i + 1}번째 숫자를 입력하세요: "))
    numbers.append(num)


sorted_numbers = sorted(numbers)


print("입력한 숫자들:", numbers)
print("정렬된 숫자들:", sorted_numbers)