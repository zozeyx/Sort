import math
import time

# 유클리드 거리 계산 함수
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# 분할 정복 방식으로 Closest Pair 찾기
def closest_pair(points):
    if len(points) <= 1:
        return float('inf'), None, None
    
    points.sort(key=lambda x: x[0])  # x좌표 기준으로 정렬
    return closest_pair_rec(points)

# 재귀적으로 Closest Pair 찾기
def closest_pair_rec(points):
    if len(points) <= 3:
        return brute_force(points)

    mid = len(points) // 2
    mid_point = points[mid]

    dl, p1, p2 = closest_pair_rec(points[:mid])
    dr, p3, p4 = closest_pair_rec(points[mid:])

    d = min(dl, dr)
    closest_points = (p1, p2) if dl < dr else (p3, p4)

    strip = []
    for point in points:
        if abs(point[0] - mid_point[0]) < d:
            strip.append(point)

    strip.sort(key=lambda x: x[1])  # y좌표 기준으로 정렬

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) < d:
                distance = euclidean_distance(strip[i], strip[j])
                if distance < d:
                    d = distance
                    closest_points = (strip[i], strip[j])
            else:
                break

    return d, closest_points[0], closest_points[1]

# 브루트 포스 방법으로 Closest Pair 찾기
def brute_force(points):
    min_dist = float('inf')
    p1, p2 = None, None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                p1, p2 = points[i], points[j]
    return min_dist, p1, p2

# 입력 파일에서 점 읽기
def read_points_from_file(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split('\t'))  # 탭으로 구분된 좌표 읽기
            points.append((x, y))
    return points

# 메인 실행 부분
if __name__ == "__main__":
    start_time = time.time()  # 시작 시간 측정
    points = read_points_from_file("input_closest_pair.txt")  # 파일에서 점 읽기
    distance, p1, p2 = closest_pair(points)  # 가장 가까운 점 쌍 찾기
    end_time = time.time()  # 종료 시간 측정

    # 결과 출력
    print(f"가장 가까운 쌍: {p1} 및 {p2} (최단 거리: {distance})")
    print(f"Closet Pair Algorithm 실행 시간: {(end_time - start_time) * 1000:f} 밀리초")  # 밀리초 단위로 출력
