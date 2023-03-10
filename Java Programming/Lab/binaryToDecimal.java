import java.util.Scanner;
//practical 5
//in this program we will convert a binary number to decimal

public class binaryToDecimal {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a binary number: ");
        int binary = input.nextInt();
        int decimal = 0;
        int power = 0;
        while (binary != 0) {
            int lastDigit = binary % 10;
            decimal += lastDigit * Math.pow(2, power);
            power++;
            binary /= 10;
        }
        System.out.println("The decimal equivalent is: " + decimal);
    }
}