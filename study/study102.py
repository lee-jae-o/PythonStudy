def maximize_meetings(meetings):
   
    meetings.sort(key=lambda x: x['end'])

    selected_meetings = []
    last_end_time = 0

    for meeting in meetings:
        if meeting['start'] >= last_end_time:
            selected_meetings.append(meeting)
            last_end_time = meeting['end']

    return selected_meetings

if __name__ == "__main__":
    meetings = [
        {'name': 'Meeting A', 'start': 1, 'end': 3},
        {'name': 'Meeting B', 'start': 2, 'end': 5},
        {'name': 'Meeting C', 'start': 4, 'end': 6},
        {'name': 'Meeting D', 'start': 6, 'end': 8},
        {'name': 'Meeting E', 'start': 5, 'end': 7}
    ]

    selected_meetings = maximize_meetings(meetings)

    print("참석할 회의들:")
    for meeting in selected_meetings:
        print(f"{meeting['name']} - 시작 시간: {meeting['start']}, 종료 시간: {meeting['end']}")