#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

using namespace std;

// Merge Sort 함수 선언
void mergeSort(vector<int>& A, vector<int>& B, int p, int r);
void merge(vector<int>& A, vector<int>& B, int p, int q, int r);

void mergeSort(vector<int>& A, vector<int>& B, int p, int r) {
    if (p < r) {
        int q = (p + r) / 2;
        mergeSort(A, B, p, q);
        mergeSort(A, B, q + 1, r);
        merge(A, B, p, q, r);
    }
}

void merge(vector<int>& A, vector<int>& B, int p, int q, int r) {
    int i = p, j = q + 1, t = p;
    while (i <= q && j <= r) {
        if (A[i] <= A[j]) {
            B[t] = A[i];
            i++;
        } else {
            B[t] = A[j];
            j++;
        }
        t++;
    }
    while (i <= q) {
        B[t] = A[i];
        t++;
        i++;
    }
    while (j <= r) {
        B[t] = A[j];
        t++;
        j++;
    }
    for (int k = p; k <= r; k++) {
        A[k] = B[k];
    }
}

int main() {
    // input_sort.txt에서 데이터 읽기
    ifstream inputFile("input_sort.txt");
    vector<int> data;
    int number;
    
    while (inputFile >> number) {
        data.push_back(number);
    }
    inputFile.close();

    vector<int> aux(data.size());
    
    // Merge Sort 실행 시간 측정
    auto start = chrono::high_resolution_clock::now();
    mergeSort(data, aux, 0, data.size() - 1);
    auto end = chrono::high_resolution_clock::now();
    
    chrono::duration<double> running_time = end - start;
    cout << "Merge Sort 실행 시간: " << running_time.count() << " 밀리초" << endl;

    // 정렬된 데이터를 output.txt 파일로 저장
    ofstream outputFile("output.txt");
    for (size_t i = 0; i < data.size(); ++i) {
        outputFile << data[i] << endl;
    }
    outputFile.close();

    cout << "정렬 결과가 output_merge_sort.txt 파일에 저장되었습니다." << endl;

    return 0;
}
