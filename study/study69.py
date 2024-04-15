def max_subarray_sum(nums):
    max_sum = float('-inf')  # 최대 합을 음의 무한대로 초기화
    n = len(nums)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(nums)
    print("가장 큰 수를 찾는 최대 서브배열 합:", result)