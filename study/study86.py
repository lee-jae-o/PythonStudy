def max_travel_destinations(destinations, budget, vacation_days):
    affordable_destinations = []


    for destination in destinations:
        if destination['cost'] <= budget:
            affordable_destinations.append(destination)


    affordable_destinations.sort(key=lambda x: x['days'])

    total_destinations = 0
    remaining_budget = budget
    remaining_days = vacation_days


    for destination in affordable_destinations:
        if destination['days'] <= remaining_days and destination['cost'] <= remaining_budget:
            total_destinations += 1
            remaining_budget -= destination['cost']
            remaining_days -= destination['days']
        else:
            break

    return total_destinations

if __name__ == "__main__":
    destinations = [
        {'name': '파리', 'cost': 500, 'days': 3},
        {'name': '로마', 'cost': 400, 'days': 2},
        {'name': '런던', 'cost': 600, 'days': 4},
        {'name': '도쿄', 'cost': 700, 'days': 5},
        {'name': '뉴욕', 'cost': 800, 'days': 3}
    ]

    budget = 1500
    vacation_days = 7

    max_destinations = max_travel_destinations(destinations, budget, vacation_days)
    print("주어진 예산과 휴가 기간 내에서 최대한 많이 방문할 수 있는 여행지의 수:", max_destinations)