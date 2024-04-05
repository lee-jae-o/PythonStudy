def is_anagram(str1, str2):
    # 두 문자열의 길이가 다르면 아나그램 관계일 수 없음
    if len(str1) != len(str2):
        return False
    
    # 각 문자열의 문자 빈도를 저장하는 딕셔너리 생성
    freq1 = {}
    freq2 = {}

    # 첫 번째 문자열의 문자 빈도를 계산
    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1
    
    # 두 번째 문자열의 문자 빈도를 계산
    for char in str2:
        freq2[char] = freq2.get(char, 0) + 1
    
    # 두 문자열의 문자 빈도가 동일한지를 확인하여 아나그램 여부를 반환
    return freq1 == freq2

if __name__ == "__main__":
    # 사용자로부터 두 개의 문자열을 입력받음
    str1 = input("첫 번째 문자열을 입력하세요: ")
    str2 = input("두 번째 문자열을 입력하세요: ")
    
    # 두 문자열이 아나그램 관계에 있는지를 판별하여 결과를 출력
    if is_anagram(str1, str2):
        print("입력한 두 문자열은 아나그램 관계입니다.")
    else:
        print("입력한 두 문자열은 아나그램 관계가 아닙니다.")