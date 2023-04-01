import java.util.ArrayList;
import java.util.Scanner;

public class PrimeNumbers {
    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        if (number == 2 || number == 3) {
            return true;
        }
        if (number % 2 == 0) {
            return false;
        }
        int sqrt = (int) Math.sqrt(number);
        for (int i = 3; i <= sqrt; i += 2) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the input number: ");
        int inputNumber = input.nextInt();

        ArrayList<Integer> primeList = new ArrayList<Integer>();
        primeList.add(2);
        for (int i = 1; i < 1000; i = i + 2) {
            if (isPrime(i)) {
                primeList.add(i);
            }
        }
        for (int i = 0; i < inputNumber; i++) {
            System.out.print(primeList.get(i) + " ");
        }
        input.close();
    }
}

