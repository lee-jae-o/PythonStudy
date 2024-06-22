def min_coins(coins, amount):
  
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    amount = int(input("교환할 금액을 입력하세요: ").strip())

    result = min_coins(coins, amount)
    if result != -1:
        print(f"최소 동전 개수: {result}개")
    else:
        print("해당 금액을 만들 수 없습니다.")
