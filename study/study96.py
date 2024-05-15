def find_intersection(list1, list2):
    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common_elements = find_intersection(list1, list2)
    print("두 리스트에 모두 포함되는 요소:", common_elements)