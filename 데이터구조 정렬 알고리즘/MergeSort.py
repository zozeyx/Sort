def mergeSortFast(A, B, p:int, r:int): #mergeSortFast함수 정의 리스트 A, 보조 리스트 B, 시작 인덱스 p, 끝 인덱스 r로 설정
    if p < r:                          #만약 p가 r보다 작다면
        q = (p+r) // 2                 #변수 q에 p+r의 중간 인덱스 값을 할당 왜냐면 정렬 범위를 절반으로 나누기 위해서
        mergeSortFast(A, B, p, q)      #정렬 범위를 반으로 나눠 왼쪽 절반에 대해 재귀호출
        mergeSortFast(A, B, q+1,r)     #정렬 범위를 반으로 나눠 오른쪽 절반에 대해 재귀호출
        mergeFast(A, B, p, q,r)        #mergeFast를 호출하여 왼쪽 절반과 오른쪽 절반을 병합

def mergeFast(A, B, p:int, q:int, r:int): 
    i = p; j = q+1; t = p                #i,j,t의 값 지정
    while i <= q and j <= r:             #i가 q이하 이고 j가 r이하 이면 반복
        if A[i] <= A[j]:                 #만약 A의 i번쨰 요소가 A가 J번째 여소보다 작거나 같을 때
            B[t] = A[i]; i += 1          #B의 t번째 위치에 A의 i번째 원소를 저장하고 i를 1증가
        else:                            #만약 아니라면
            B[t] = A[j]; j +=1;          #B의 t번째 위치에 A의 j번째 원소를 저장하고 j를 1증가
        t += 1                           #t를 1증가
    while i <= q:                        #i가 q보다 작거나 같으면 반복
        B[t] = A[i]; t += 1; i += 1      #B의 t번째 위치에 A의 i번째 원소를 저장, t,i를 1증가
    while j <= r:                        #j가 r보다 작거나 같으면 반복
        B[t] = A[j]; t += 1; j += 1      #B의 t번째 위치에 A의 j번째 원소를 저장, t,j를 1증가
    for k in range(p, r+1):              #p부터 r까지 반복
        A[k] = B[k]                      #A의 k번째 위치에 B의 k번째 값을 복사