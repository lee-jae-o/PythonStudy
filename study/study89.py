def count_rides(children_heights, rides):
    ride_counts = [0] * len(rides)

    for child_height in children_heights:
        for i, ride in enumerate(rides):
            min_height, max_height = ride
            if min_height <= child_height <= max_height:
                ride_counts[i] += 1

    max_rides = max(ride_counts)
    return max_rides

if __name__ == "__main__":
    children_heights = [130, 140, 150, 160]
    rides = [(120, 140), (130, 150), (140, 160), (150, 170)]

    max_rides = count_rides(children_heights, rides)
    print("아이들이 가장 많이 탈 수 있는 놀이기구의 수:", max_rides)