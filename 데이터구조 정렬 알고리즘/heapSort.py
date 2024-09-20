def heapSort(A):                                #heapSort 함수 정의            
    buildHeap(A)                                #buildHeap 호출
    for last in range(len(A) - 1, 0, -1):       #리스트의 마지막부터 첫번째 요소까지 역순으로 반복
        A[last], A[0] = A[0], A[last]           #A의 last번째(현재) 요소랑 A의 첫번째 요소를 교환
        percolateDown(A, 0, last-1)             #percolateDown함수 호출

def buildHeap(A):                               #buildHeap 함수 정의(리스트를 힙 구조로 변환)
    for i in range((len(A) - 2) // 2, -1, -1):  #리스트의 중간요소부터 첫번째 요소까지 반복
        percolateDown(A, i, len(A) - 1)         #percolateDown함수 호출
    
def percolateDown(A, k:int, end:int):           #percolateDown함수 정의
    left = 2*k+1                                #left값 정의(왼쪽 자식)
    right = 2*k+2                               #right값 정의(오른쪽 자식)
    if left <= end:                             #만약 left가 end보다 작거나 같다면
        if right <= end and A[left] < A[right]: #만약 right가 end보다 작거나 같고 A의 left번째 요소가 A의 right번쨰 요소보다 작다면
            left = right                        #right값을 left에 할당
        if A[k] < A[left]:                      #만약 A의 k번째 요소가 left보다 작다면
            A[k], A[left] = A[left],A[k]        #A의 k번째 요소와 left번째 요소를 교환
            percolateDown(A,left,end)           #재귀 호출