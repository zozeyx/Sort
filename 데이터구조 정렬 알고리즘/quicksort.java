import java.io.*;
import java.util.*;

public class quicksort {

    public static void main(String[] args) {
        List<Integer> numbers = readNumbersFromFile("input_sort.txt");
        
        long startTime = System.currentTimeMillis(); // 시간 측정 시작
        quickSort(numbers, 0, numbers.size() - 1);
        long endTime = System.currentTimeMillis(); // 시간 측정 종료
        
        writeNumbersToTextFile(numbers, "output_quick_sort.txt");
        
        System.out.println("정렬 완료: " + durationInMillis + " 밀리초");
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

    public static void writeNumbersToTextFile(List<Integer> numbers, String filename) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filename))) {
            for (int number : numbers) {
                writer.write(number + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
