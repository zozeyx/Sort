from selectionSort import *
import random
import time
import sys



B=[2,1,4,6,8]

def selectionSortRec(A, n):         # 길이 n을 가지는 A[0,1,..n-1] 리스트의 선택정렬(재귀)
    if (n>1):
        k= theLargest4Rec(A, n)   # 0에서 n-1까지에서의 최대값 찾기
        A[k], A[n-1] = A[n-1], A[k] # 최대값 원소 A[k]와 마지막 원소 A[n-1] 교환
        selectionSortRec(A, n-1)    # 원소의 길이가 하나 줄어든 자신의 재귀호출


def theLargest4Rec(A, last:int) -> int:	# A[0...last]에서 가장 큰 수의 인덱스를 리턴한다
	largest = 0					   #largest을 0으로 초기화
	for i in range(last):          #last-1 까지 반복
		if A[i] > A[largest]:	   #리스트 A의 i번째 요소가 A의 largest번째 요소보다 크다면
			largest = i			   #largest에 i값을 할당
	return largest				   #largest값을 반환

selectionSortRec(B,5)
print(B)
