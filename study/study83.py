def find_combinations_with_sum(nums, target):
    combinations = []

    # 리스트의 모든 요소를 탐색하여 가능한 모든 조합을 찾습니다.
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                combinations.append((nums[i], nums[j]))

    return combinations

if __name__ == "__main__":
    nums = [2, 4, 6, 8, 10]
    target_sum = 12

    result = find_combinations_with_sum(nums, target_sum)
    print(f"합이 {target_sum}이 되는 모든 조합은:")
    for combination in result:
        print(combination)