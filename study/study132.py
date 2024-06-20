def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("정렬된 배열:", arr)
    target = int(input("찾고 싶은 숫자를 입력하세요: ").strip())

    result = binary_search(arr, target)

    if result != -1:
        print(f"숫자 {target}은(는) 인덱스 {result}에 있습니다.")
    else:
        print(f"숫자 {target}을(를) 배열에서 찾을 수 없습니다.")
