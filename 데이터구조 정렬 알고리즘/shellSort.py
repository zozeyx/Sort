def shellSort(A):                           #shellSort함수 정의
    H = gapSequence(len(A))                 #gapSeQuence함수를 H에 할당
    for h in H:                             #H를 통해 간격 h를 반복
        for k in range(h):                  #k를 0부터 h-1까지 반복
            stepInsertionSort(A,k,h)        #stepInsertionSort함수 호출

def stepInsertionSort(A, k: int , h: int):  #stepInsertionSort 함수 정의
    for i in range(k + h, len(A), h):       #i를 k+h부터 len(A)-1까지 h간격으로 반복
        j = i - h                           #i-h값을 j에 할당
        newItem = A[i]                      #A의 i번째 값을 newItem에 할당
        while 0 <= j and newItem < A[j]:    #j가 0보다 크고 newItem 값이 A의j번째 값보다 작을때 반복
            A[j + h] = A[j]                 #A의 j+h번째 값에 A의j번째 값을 대입
            j -= h                          #j를 h만큼 감소
        A[j + h] = newItem                  #A의 j+h번째 값에 newItem 값을 삽입

def gapSequence(n: int) -> list:            #gapSequence함수 정의
    H = [1]; gap = 1                        #H리스트 정의, gap값 정의
    while gap < n/5:                        #gap값이 n/5 보다 작을때까지 반복
        gap = 3 * gap + 1                   #gap값을 3*gap +1로 업데이트
        H.append(gap)                       #H리스트에 gap값 삽입
    H.reverse()                             #H리스트 역순으로 뒤집기
    return H                                #H리스트 반환