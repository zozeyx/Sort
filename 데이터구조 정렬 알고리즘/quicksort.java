import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.*;
import java.util.*;

public class QuickSortExample {

    public static void main(String[] args) {
        List<Integer> numbers = readNumbersFromFile("input_sort.txt");
        
        long startTime = System.nanoTime(); // 시간 측정 시작
        quickSort(numbers, 0, numbers.size() - 1);
        long endTime = System.nanoTime(); // 시간 측정 종료

        writeNumbersToExcel(numbers, "output_quick_sort.xlsx");
        
        System.out.println("정렬 완료: " + (endTime - startTime) + " 나노초");
    }

    public static List<Integer> readNumbersFromFile(String filename) {
        List<Integer> numbers = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                numbers.add(Integer.parseInt(line));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return numbers;
    }

    public static void quickSort(List<Integer> A, int p, int r) {
        if (p < r) {
            int q = partition(A, p, r);
            quickSort(A, p, q - 1);
            quickSort(A, q + 1, r);
        }
    }

    public static int partition(List<Integer> A, int p, int r) {
        int x = A.get(r);
        int i = p - 1;
        for (int j = p; j < r; j++) {
            if (A.get(j) < x) {
                i++;
                Collections.swap(A, i, j);
            }
        }
        Collections.swap(A, i + 1, r);
        return i + 1;
    }

    public static void writeNumbersToExcel(List<Integer> numbers, String filename) {
        Workbook workbook = new XSSFWorkbook(); // 새로운 엑셀 워크북 생성
        Sheet sheet = workbook.createSheet("Sorted Numbers"); // 시트 생성

        for (int i = 0; i < numbers.size(); i++) {
            Row row = sheet.createRow(i); // 새로운 행 생성
            Cell cell = row.createCell(0); // 첫 번째 열에 셀 생성
            cell.setCellValue(numbers.get(i)); // 셀에 값 설정
        }

        try (FileOutputStream fileOut = new FileOutputStream(filename)) {
            workbook.write(fileOut); // 엑셀 파일로 쓰기
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                workbook.close(); // 워크북 닫기
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
