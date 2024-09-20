from selectionSort import *   
from bubbleSort import *
from insertionSort import *
from MergeSort import *
from QuickSort import *
from heapSort import *
from shellSort import *
import random
import time
import sys

sys.setrecursionlimit(1000000)          #재귀 호출 한계값 설정
listLength= 300                         #리스트 길이를 300으로 설정
num = 1000                              #반복횟수 변수 설정(1000번)

sel_total = 0                           #선택정렬 총 걸리는 시간 변수 초기화
for i in range(num):                    #num 만큼 반복(1000번 반복)
    B=[]                                #빈 리스트
    for value in range(0,listLength):   #listLength만큼 반복(300번 반복)
          B.append(random.randint(0,100)) #0부터 100까지 랜덤한수 B리스트에 추가
    A= B                                #리스트 B를 리스트 A에 할당
    start= time.time()                  #현재시간을 시작시간으로 설정
    selectionSortRec(A, listLength)     #선택정렬(재귀적) 호출
    end= time.time()                    #끝난시간 설정
    sel_total += end-start              #sel_total에 함수 걸리는시간 계속 더하기
sel_aver = sel_total / num              #총 sel_total에 num 나누기(평균 시간 구하기)

print('selection Sort average Time : ',sel_aver) #선택정렬(재귀적) 평균시간 화면 출력


bub_total = 0                           #버블정렬 총 걸리는 시간 변수 초기화
for i in range(num):                    #num만큼 반복(1000번 반복)
    B=[]                                #빈 리스트 생성
    for value in range(0,listLength):   #listLength만큼 반복(300번 반복)
          B.append(random.randint(0,100)) #0부터 100까지 랜덤한수 B리스트에 추가
    A= B                                #리스트 B를 리스트 A에 할당
    start= time.time()                  #현재시간을 시작시간으로 설정
    bubbleSortRec(A,listLength)         #버블정렬(재귀적) 호출
    end= time.time()                    #끝난시간 설정
    bub_total += end-start              #bub_total에 정렬이 걸리는시간 계속 더하기
bub_aver = bub_total / num              #bub_total에 num 나누기(평균 시간 구하기)

print('bubble Sort average Time : ',bub_aver) #버블정렬*재귀적) 평균 시간 화면 출력  


ins_total = 0                           #삽입정렬 총 걸리는 시간 변수 초기화
for i in range(num):                    #num 만큼 반복(1000번 반복)
    B=[]                                #빈 리스트 생성
    for value in range(0,listLength):   #listLength만큼 반복(300번 반복)
          B.append(random.randint(0,100))#0부터 100까지 랜덤한수 B리스트에 추가하기
    A=B.copy()                          #리스트 B를 리스트 A에 할당
    start= time.time()                  #현재시간을 시작시간으로 설정
    insertionSortRec(A, 0,len(A))       #삽입정렬(재귀적) 호출
    end= time.time()                    #끝난시간 설정
    ins_total += end-start              #ins_total에 걸리는 시간 계속 더하기기
ins_aver = ins_total / num              #ins_total에 num 나누기 (평균 시간 구하기)

print('Insertion Sort average Time : ',ins_aver) #삽입정렬(재귀적) 평균 시간 화면 출력

mer_total = 0                          #병합정렬 총 걸리는 시간 변수 초기화
for i in range(num):                   #num 만큼 반복(1000번 반복)
    B=[]                               #빈 리스트 생성
    for value in range(0,listLength):  #listLength만큼 반복(300번 반복)
          B.append(random.randint(0,100))#0부터 100까지 랜덤한수 B리스트에 추가하기
    A=B.copy()                         #리스트 A가 리스트 B 카피
    start=time.time()                  #현재시간을 시작시간으로 설정
    C = [None]* len(A)                 #C에 리스트 A길이만큼(300) 요소를 None으로 가지고있는 리스트 생성
    mergeSortFast(A, C, 0, len(A)-1)   #재귀적 병합정렬(비효율성 개선) 호출
    end=time.time()                    #끝난시간 설정
    mer_total += end-start             #mer_total에 걸리는시간 계속 더하기
mer_aver = mer_total / num             #mer_total에 num 나누기 (평균 시간 구하기)

print('Merge Sort average Time : ',mer_aver) #병합정렬(재귀적) 평균 시간 화면에 출력


quick_total = 0                        #퀵정렬 총 걸리는 시간 변수 초기화
for i in range(num):                   #num 만큼 반복(1000번 반복)
    B=[]                               #빈 리스트 생성
    for value in range(0,listLength):  #listLength만큼 반복(300번 반복)
          B.append(random.randint(0,100))#0부터 100까지 랜덤한수 B리스트에 추가하기
    A= B.copy()                         #리스트 A가 리스트 B 카피
    start= time.time()                  #현재시간을 시작시간으로 설정
    quickSort(A, 0,len(A)-1)            #퀵 정렬 호출
    end= time.time()                    #끝난시간 설정
    quick_total += end-start            #quick_total에 걸리는시간 계속 더하기
quick_aver = quick_total / num          #quick_total에 num 나누기(평균 시간 구하기)

print('Quick Sort average Time : ',quick_aver) #퀵 정렬 평균 시간 화면에 출력


heap_total = 0                          #힙 정렬 총 걸리는 시간 변수 초기화
for i in range(num):                    #num 만큼 반복(1000번 반복)
    B=[]                                #빈 리스트 생성
    for value in range(0,listLength):   #listLength만큼 반복(300번 반복)
          B.append(random.randint(0,100))#0부터 100까지 랜덤한수 B리스트에 추가하기
    A= B                                #리스트 B를 리스트 A에 할당
    start= time.time()                  #현재시간을 시작시간으로 설정
    heapSort(A)                         #힙 정렬 호출
    end= time.time()                    #끝난시간 설정
    heap_total += end-start             #heap_total에 걸리는 시간 계속 더하기
heap_aver = heap_total / num            #heap_total에 num 나누기(평균 시간 구하기)

print('Heap Sort average Time : ',heap_aver) #힙 정렬 평균 시간 화면에 출력


shell_total = 0                         #쉘 정렬 총 걸리는 시간 변수 초기화
for i in range(num):                    #num 만큼 반복(1000번 반복)
    B=[]                                #빈 리스트 생성
    for value in range(0,listLength):   #listLength만큼 반복(300번 반복)
          B.append(random.randint(0,100))#0부터 100까지 랜덤한수 B리스트에 추가하기
    A= B                                #리스트 B를 리스트 A에 할당
    start= time.time()                  #현재시간을 시작시간으로 설정
    shellSort(A)                        #쉘 정렬 호출
    end= time.time()                    #끝난시간 설정
    shell_total += end-start            #shell_total에 걸리는 시간 계속 더하기
shell_aver = shell_total / num          #shell_total에 num 나누기 (평균 시간 구하기)

print('Shell Sort average Time : ',shell_aver) #쉘 정렬 평균 시간 화면에 출력

