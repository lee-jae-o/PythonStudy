def 첫글자대문자변환(문자열):
    단어들 = 문자열.split()
    변환된_단어들 = [단어.capitalize() for 단어 in 단어들]
    return ' '.join(변환된_단어들)

if __name__ == "__main__":
    입력문자열 = input("문자열을 입력하세요: ")
    결과문자열 = 첫글자대문자변환(입력문자열)

    print("첫 글자 대문자 변환 결과:", 결과문자열)