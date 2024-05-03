def max_subarray_sum(nums):
    max_sum = nums[0]  # 첫 번째 요소로 초기화
    current_sum = nums[0]

    # 리스트를 순회하면서 최대 부분 리스트의 합을 찾습니다.
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    result = max_subarray_sum(nums)
    print("가장 큰 연속된 부분 리스트의 합은:", result)