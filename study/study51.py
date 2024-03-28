def 피보나치(n):
    if n <= 1:
        return n
    else:
        return 피보나치(n-1) + 피보나치(n-2)

if __name__ == "__main__":
    n = int(input("몇 번째 피보나치 수를 계산할까요? "))
    
    if n <= 0:
        print("양수를 입력해주세요.")
    else:
        결과 = 피보나치(n)
        print(f"{n}번째 피보나치 수는 {결과}입니다.")