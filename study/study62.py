def longest_repeating_substring(s):
    n = len(s)
    longest_substring = ""
    
    # 부분 문자열의 길이를 이진 탐색으로 결정합니다.
    left, right = 1, n
    while left <= right:
        mid = left + (right - left) // 2
        seen = set()
        found = False
        
        # 길이가 mid인 모든 부분 문자열을 검사합니다.
        for i in range(n - mid + 1):
            substring = s[i:i+mid]
            if substring in seen:
                found = True
                longest_substring = substring
                break
            else:
                seen.add(substring)
        
        if found:
            left = mid + 1
        else:
            right = mid - 1
    
    return longest_substring

if __name__ == "__main__":
    input_string = input("문자열을 입력하세요: ")
    result = longest_repeating_substring(input_string)
    
    if result:
        print("가장 긴 반복되는 부분 문자열:", result)
    else:
        print("반복되는 부분 문자열이 없습니다.")