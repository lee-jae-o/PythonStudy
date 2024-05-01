def total_time_to_return(home_to_work_time, meeting_time):
    return home_to_work_time + meeting_time

if __name__ == "__main__":
    home_to_work_time = int(input("출근 시간에 걸리는 시간(분): "))
    meeting_time = int(input("회의 시간(분): "))

    total_time = total_time_to_return(home_to_work_time, meeting_time)
    print(f"회의가 끝난 후 집에 돌아가기 위해 필요한 총 시간은 {total_time}분입니다.")