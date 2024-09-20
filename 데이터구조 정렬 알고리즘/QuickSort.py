def quickSort(A, p:int, r:int): #quickSort 함수 정의 A= 리스트, p=시작인덱스, r=끝 인덱스
    if p < r:                   #p가 r보다 작을 때
        q = partition(A,p,r)    #partition 함수 반환값을 q에 저장
        quickSort(A,p,q-1)      #p부터 q-1(왼쪽부분) 리스트 재귀호출
        quickSort(A,q+1,r)      #q+1부터 r(오른쪽부분) 리스트 재귀호출
    
def partition(A,p:int,r:int) -> int:    #partition 함수 정의
    x = A[r]                            #x는 A의 r번째 요소
    i = p-1                             #i는 p-1번째 값
    for j in range(p,r):                #p부터 r-1까지 반복
        if A[j] < x:                    #만약 A의 j번째 요소가 x보다 작다면
            i += 1                      #i를 1증가
            A[i], A[j] = A[j], A[i]     #A의 i번째 요소와 A의 j번째 요소 교환
        elif A[j] == x:                 #만약 A의 j번째 요소가 x와 같다면
            if j % 2 == 0:              #만약 j가 짝수라면
                i += 1                  #i를 1증가
            else:                       #만약 j가 짝수가 아니라면
                i += 1                  #i를 1증가
                A[i], A[j] = A[j], A[i] #A의 i번째 요소와 A의 j번째 요소 교환
    A[i+1], A[r] = A[r], A[i+1]         #A의 i+1번쨰 요소와 A의 r번째 요소 교환(x값을 기준으로 작은건 왼쪽 큰건 오른쪽으로 위치)
    return i+1                          #함수의 반환값으로 i+1 반환
