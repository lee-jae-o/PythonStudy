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
    arr = [2, 3, 4, 10, 40]
    target = 2
    result = binary_search(arr, target)
    if result != -1:
        print(f"원소 {target}은(는) 인덱스 {result}에 위치합니다.")
    else:
        print("원소를 찾을 수 없습니다.")