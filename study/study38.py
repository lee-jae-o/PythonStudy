def 모음과자음개수세기(문자열):
    모음 = 0
    자음 = 0
    for 문자 in 문자열:
        if 문자.lower() in 'aeiou':
            모음 += 1
        elif 문자.isalpha():
            자음 += 1
    return 모음, 자음

if __name__ == "__main__":
    입력문자열 = input("문자열을 입력하세요: ")
    모음개수, 자음개수 = 모음과자음개수세기(입력문자열)

    print(f"모음 개수: {모음개수}")
    print(f"자음 개수: {자음개수}")
