def count_attractions(children_heights, attractions):
    attraction_counts = [0] * len(attractions)

    for child_height in children_heights:
        for i, attraction in enumerate(attractions):
            min_height, max_height = attraction
            if min_height <= child_height <= max_height:
                attraction_counts[i] += 1

    max_attractions = max(attraction_counts)
    return max_attractions

if __name__ == "__main__":
    children_heights = [110, 120, 130, 140]
    attractions = [(100, 120), (110, 130), (120, 140), (130, 150)]

    max_attractions = count_attractions(children_heights, attractions)
    print("아이들이 가장 많이 이용할 수 있는 놀이시설의 수:", max_attractions)