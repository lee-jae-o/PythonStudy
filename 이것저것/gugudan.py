def dan(i):
    print("---", i, "단", "---")
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)

num = int(input("출력하고 싶은 구구단의 단을 입력하세요: "))
print("")

dan(num)
