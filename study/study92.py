def count_campgrounds(travel_schedule, campgrounds):
    campground_counts = [0] * len(campgrounds)

    for day in travel_schedule:
        for i, campground in enumerate(campgrounds):
            start_date, end_date = campground
            if start_date <= day <= end_date:
                campground_counts[i] += 1

    max_campgrounds = max(campground_counts)
    return max_campgrounds

if __name__ == "__main__":
    travel_schedule = [3, 5, 8, 10, 12]  
    campgrounds = [(1, 4), (4, 7), (6, 9), (8, 12)]  

    max_campgrounds = count_campgrounds(travel_schedule, campgrounds)
    print("가족들이 최대로 방문할 수 있는 캠핑장의 수:", max_campgrounds)