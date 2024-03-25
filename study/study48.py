def 회문_판별(문자열):
    정제된_문자열 = ''.join(문자.lower() for 문자 in 문자열 if 문자.isalnum())
    return 정제된_문자열 == 정제된_문자열[::-1]

if __name__ == "__main__":
    입력문자열 = input("문자열을 입력하세요: ")
    
    if 회문_판별(입력문자열):
        print("입력한 문자열은 회문입니다.")
    else:
        print("입력한 문자열은 회문이 아닙니다.")