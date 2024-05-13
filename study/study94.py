import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

if __name__ == "__main__":
    point1 = (1, 2)
    point2 = (4, 6)
    distance = calculate_distance(point1, point2)
    print(f"두 지점 사이의 최단 거리는 {distance:.2f}입니다.")