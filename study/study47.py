def 첫_반복되지_않는_문자(문자열):
    문자_카운트 = {}

    for 문자 in 문자열:
        if 문자 in 문자_카운트:
            문자_카운트[문자] += 1
        else:
            문자_카운트[문자] = 1

    for 문자 in 문자열:
        if 문자_카운트[문자] == 1:
            return 문자

    return None

if __name__ == "__main__":
    입력문자열 = input("문자열을 입력하세요: ")
    결과 = 첫_반복되지_않는_문자(입력문자열)

    if 결과:
        print("첫 번째로 반복되지 않는 문자:", 결과)
    else:
        print("반복되지 않는 문자가 없습니다.")