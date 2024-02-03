students = []


num_students = int(input("학생 수를 입력하세요: "))
for i in range(num_students):
    name = input(f"{i + 1}번 학생 이름: ")
    score = float(input(f"{name}의 성적을 입력하세요: "))
    students.append({"이름": name, "성적": score})


total_score = sum(student["성적"] for student in students)
average_score = total_score / num_students


print("\n학생 성적 및 평균 성적:")
for student in students:
    print(f"{student['이름']}: {student['성적']}")
print(f"\n평균 성적: {average_score}")