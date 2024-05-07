def find_duplicates(nums):

    unique_nums_set = set(nums)
    

    duplicates = []


    if len(nums) != len(unique_nums_set):
       
        for num in unique_nums_set:
            if nums.count(num) > 1:
                duplicates.append(num)

    return duplicates

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 5]

    duplicate_numbers = find_duplicates(numbers)
    print("중복된 숫자:", duplicate_numbers)