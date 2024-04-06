def most_frequent_character(s):
    # 빈도를 저장할 딕셔너리를 생성합니다.
    freq = {}
    
    # 문자열을 순회하면서 각 문자의 빈도를 계산합니다.
    for char in s:
        if char.isalpha():  # 알파벳인 경우에만 빈도를 계산합니다.
            char = char.lower()  # 대소문자를 구분하지 않습니다.
            freq[char] = freq.get(char, 0) + 1
    
    # 가장 많이 등장하는 문자를 찾습니다.
    max_freq = max(freq.values())
    most_frequent_chars = [char for char, frequency in freq.items() if frequency == max_freq]
    
    return most_frequent_chars

if __name__ == "__main__":
    input_string = input("문자열을 입력하세요: ")
    result = most_frequent_character(input_string)
    
    if result:
        print("가장 많이 등장하는 문자:", result)
    else:
        print("알파벳 문자가 없습니다.")