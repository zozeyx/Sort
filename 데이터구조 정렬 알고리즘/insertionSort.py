def insertionSortRec(A, start,end): #삽입정렬 함수 정의 리스트 A, 시작 인덱스 start, 끝 인덱스 end
    value=A[start]                  #리스트 A의 시작 인덱스를 'value'에 저장
    loc = start                     #변수 loc에 start값을 할당
    while loc > 0 and A[loc - 1] > value:   #loc가 0보다 크고 리스트 A의 loc-1번째 요소가 value보다 크다면
        A[loc] = A[loc - 1]         #리스트 A의 loc인덱스에 현재 위치의 이전 위치에 해당하는 값 대입
        loc -= 1                    #loc값을 1 감소
    A[loc] = value                  #리스트 A의 loc인덱스에 value 값을 대입

    if start + 1 < end:             #만약 start +1 값이 end 보다 작다면
        insertionSortRec(A,start+1,end) #삽입정렬 재귀호출