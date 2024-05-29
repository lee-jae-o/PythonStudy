from datetime import datetime, timedelta

def calculate_parking_fee(entry_time, exit_time, base_fee=2000, hourly_fee=500):
    total_fee = base_fee
    parked_duration = exit_time - entry_time
    parked_hours = parked_duration.total_seconds() // 3600

    if parked_duration.total_seconds() % 3600 > 0:
        parked_hours += 1

    total_fee += parked_hours * hourly_fee

    return total_fee

if __name__ == "__main__":
    entry_time = datetime(2024, 5, 29, 8, 30)  
    exit_time = datetime(2024, 5, 29, 13, 45)  

    total_fee = calculate_parking_fee(entry_time, exit_time)

    print(f"주차 시작 시간: {entry_time.strftime('%Y-%m-%d %H:%M')}")
    print(f"주차 종료 시간: {exit_time.strftime('%Y-%m-%d %H:%M')}")
    print(f"총 주차 요금: {total_fee}원")