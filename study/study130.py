def find_most_frequent_char(input_str):
    char_count = {}
    
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    

    max_char = ''
    max_count = 0
    
    for char, count in char_count.items():
        if count > max_count:
            max_char = char
            max_count = count
    
    return max_char, max_count

if __name__ == "__main__":
    input_string = "you are so cute"
    most_frequent_char, frequency = find_most_frequent_char(input_string)
    
    print(f"주어진 문자열 '{input_string}'에서 가장 많이 등장한 문자는 '{most_frequent_char}'입니다.")
    print(f"등장 횟수는 총 {frequency}번입니다.")
