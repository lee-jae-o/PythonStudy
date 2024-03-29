def 최대_부분_배열_합(리스트):
    현재_최대_합 = 최종_최대_합 = 리스트[0]

    for 숫자 in 리스트[1:]:
        현재_최대_합 = max(숫자, 현재_최대_합 + 숫자)
        최종_최대_합 = max(최종_최대_합, 현재_최대_합)

    return 최종_최대_합

if __name__ == "__main__":
    숫자_리스트 = [1, -3, 5, -2, 9, -8, -6, 29]
    최대_합 = 최대_부분_배열_합(숫자_리스트)
    print("최대 부분 배열의 합:", 최대_합)