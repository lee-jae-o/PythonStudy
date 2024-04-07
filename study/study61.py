def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i, j = 0, 0

    # 두 배열을 순회하면서 작은 값을 merged_array에 추가
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    
    # 남은 요소를 merged_array에 추가
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

if __name__ == "__main__":
    arr1 = list(map(int, input("첫 번째 정렬된 배열을 입력하세요 (공백으로 구분): ").split()))
    arr2 = list(map(int, input("두 번째 정렬된 배열을 입력하세요 (공백으로 구분): ").split()))
    
    merged = merge_sorted_arrays(arr1, arr2)
    print("병합된 정렬된 배열:", merged)