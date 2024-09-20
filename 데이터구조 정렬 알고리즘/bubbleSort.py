def bubbleSortRec(A, n):    #버블정렬(재귀적) 함수 정의
    for i in range(n-1):    #0부터 n-1까지 반복
        if A[i] > A[i+1]:   #리스트 A의 i번째 요소가 i+1번째 요소보다 크다면
            A[i], A[i+1] = A[i+1], A[i] #리스트 A의 i번째 요소와 i+1번째 요소의 위치를 서로 교환
    if n > 1:                   # n=2까지 재귀호출
        bubbleSortRec(A, n-1)   # 재귀호출 
    