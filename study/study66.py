def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 배열을 반으로 나누기
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 왼쪽과 오른쪽 부분 배열을 재귀적으로 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # 정렬된 부분 배열을 병합
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_pointer = right_pointer = 0
    
    # 왼쪽과 오른쪽 부분 배열을 비교하며 작은 값을 병합
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            merged.append(left[left_pointer])
            left_pointer += 1
        else:
            merged.append(right[right_pointer])
            right_pointer += 1
    
    # 남은 요소들을 추가
    merged.extend(left[left_pointer:])
    merged.extend(right[right_pointer:])
    
    return merged

if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 5, 7, 9, 4]
    sorted_arr = merge_sort(arr)
    print("정렬된 배열:", sorted_arr)