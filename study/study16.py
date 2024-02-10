def reverse_name():
    # 사용자에게 이름 입력 받기
    name = input("이름을 입력하세요: ")

    # 이름 반전 및 출력
    reversed_name = " ".join(name.split()[::-1])
    print("반전된 이름:", reversed_name)

if __name__ == "__main__":
    reverse_name()