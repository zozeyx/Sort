import time
import math

def read_coordinates_from_file(filename):
    with open(filename, 'r') as file:
        coordinates = [tuple(map(int, line.split())) for line in file]
    # 중복 좌표 제거
    unique_coordinates = list(set(coordinates))
    return unique_coordinates

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(points):
    if len(points) <= 3:
        return brute_force_closest_pair(points)

    mid = len(points) // 2
    left_half = points[:mid]
    right_half = points[mid:]

    (p1, p2, d1) = closest_pair(left_half)
    (p3, p4, d2) = closest_pair(right_half)

    if d1 < d2:
        d = d1
        closest_points = (p1, p2)
    else:
        d = d2
        closest_points = (p3, p4)

    strip = [point for point in points if abs(point[0] - points[mid][0]) < d]
    
    return min_distance(strip, d, closest_points)

def min_distance(strip, d, closest_points):
    strip.sort(key=lambda point: point[1])  # y-coordinate sorting
    min_dist = d
    p1, p2 = closest_points

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            distance = euclidean_distance(strip[i], strip[j])
            if distance < min_dist:
                min_dist = distance
                p1, p2 = strip[i], strip[j]

    return (p1, p2, min_dist)

def brute_force_closest_pair(points):
    min_dist = float('inf')
    p1 = p2 = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_dist:
                min_dist = distance
                p1, p2 = points[i], points[j]
    return (p1, p2, min_dist)

def main():
    start_time = time.time()
    
    points = read_coordinates_from_file("input_closest_pair.txt")
    points.sort()  # x-coordinate sorting

    p1, p2, min_distance = closest_pair(points)

    end_time = time.time()
    running_time = (end_time - start_time) * 1000  # 밀리초로 변환

    print(f"가장 짧은 거리의 좌표 쌍: {p1}, {p2}")
    print(f"최단 거리: {min_distance:.6f}")
    print(f"실행 시간: {running_time:.6f} 밀리초")

if __name__ == "__main__":
    main()
