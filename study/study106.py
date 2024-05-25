from datetime import datetime

def filter_transactions(transactions, start_date, end_date):
    filtered_transactions = [
        transaction for transaction in transactions
        if start_date <= transaction['date'] <= end_date
    ]
    return filtered_transactions

def calculate_balance(transactions, initial_balance=0):
    balance = initial_balance
    for transaction in transactions:
        if transaction['type'] == 'deposit':
            balance += transaction['amount']
        elif transaction['type'] == 'withdrawal':
            balance -= transaction['amount']
    return balance

if __name__ == "__main__":
    transactions = [
        {'date': datetime(2024, 5, 1), 'type': 'deposit', 'amount': 1000},
        {'date': datetime(2024, 5, 3), 'type': 'withdrawal', 'amount': 200},
        {'date': datetime(2024, 5, 5), 'type': 'deposit', 'amount': 500},
        {'date': datetime(2024, 5, 10), 'type': 'withdrawal', 'amount': 300},
        {'date': datetime(2024, 5, 12), 'type': 'deposit', 'amount': 700}
    ]

    initial_balance = 1000
    start_date = datetime(2024, 5, 1)
    end_date = datetime(2024, 5, 10)

    filtered_transactions = filter_transactions(transactions, start_date, end_date)
    final_balance = calculate_balance(filtered_transactions, initial_balance)

    print("필터링된 트랜잭션:")
    for transaction in filtered_transactions:
        print(f"{transaction['date'].strftime('%Y-%m-%d')} - {transaction['type']} - {transaction['amount']}원")

    print(f"초기 잔액: {initial_balance}원")
    print(f"최종 잔액: {final_balance}원")