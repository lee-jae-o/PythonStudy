def count_toys(children_ages, toys):
    toy_counts = [0] * len(toys)

    for child_age in children_ages:
        for i, toy in enumerate(toys):
            min_age, max_age = toy
            if min_age <= child_age <= max_age:
                toy_counts[i] += 1

    max_toys = max(toy_counts)
    return max_toys

if __name__ == "__main__":
    children_ages = [5, 6, 7, 8]
    toys = [(3, 6), (4, 7), (5, 8), (6, 9)]

    max_toys = count_toys(children_ages, toys)
    print("아이들이 가장 많이 대여할 수 있는 장난감의 수:", max_toys)