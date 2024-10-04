#include <stdio.h>
#include <stdlib.h> // for malloc and free
#include <time.h>   // for clock and clock_t

// 선택 정렬 재귀 함수 선언
void selectionSortRec(int A[], int n);

// 배열에서 가장 큰 원소의 인덱스를 찾는 함수 선언
int theLargest4Rec(int A[], int last);

int main() {
    FILE *file = fopen("input_sort.txt", "r"); // 파일 열기
    if (file == NULL) {
        perror("파일 열기 실패");
        return EXIT_FAILURE;
    }

    // 파일에서 정수 읽기
    int *B = malloc(100 * sizeof(int)); // 메모리 동적 할당 (최대 100개로 가정)
    int n = 0; // 실제 읽은 숫자의 개수

    while (fscanf(file, "%d", &B[n]) != EOF && n < 100) {
        n++;
    }
    fclose(file); // 파일 닫기

    // 선택 정렬 실행 시간 측정
    clock_t start_time = clock(); // 시간 측정 시작
    selectionSortRec(B, n);
    clock_t end_time = clock(); // 시간 측정 종료

    // 50번째와 70번째 숫자 출력
    if (n >= 50) {
        printf("50번째 숫자: %d\n", B[49]); // 0-based index
    } else {
        printf("50번째 숫자가 존재하지 않습니다.\n");
    }

    if (n >= 70) {
        printf("70번째 숫자: %d\n", B[69]); // 0-based index
    } else {
        printf("70번째 숫자가 존재하지 않습니다.\n");
    }

    // 실행 시간 출력 (밀리초로 변환)
    double running_time_ms = ((double)(end_time - start_time) / CLOCKS_PER_SEC) * 1000; // 밀리초로 변환
    printf("Selection Algorithm 실행 시간: %f 밀리초\n", running_time_ms);

    free(B); // 동적 할당된 메모리 해제
    return 0;
}

// 선택 정렬 재귀 함수 정의
void selectionSortRec(int A[], int n) {
    if (n > 1) {
        int k = theLargest4Rec(A, n); // 가장 큰 원소의 인덱스를 찾음
        // 가장 큰 원소와 마지막 원소를 교환
        int temp = A[k];
        A[k] = A[n-1];
        A[n-1] = temp;
        // 원소가 하나 줄어든 배열에 대해 재귀 호출
        selectionSortRec(A, n - 1);
    }
}

// 배열에서 가장 큰 원소의 인덱스를 찾는 함수 정의
int theLargest4Rec(int A[], int last) {
    int largest = 0; // 가장 큰 원소의 인덱스 초기화
    for (int i = 1; i < last; i++) {
        if (A[i] > A[largest]) {
            largest = i; // 더 큰 원소가 있으면 largest 갱신
        }
    }
    return largest; // 가장 큰 원소의 인덱스 반환
}
