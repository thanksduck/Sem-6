//this program is to find the sum of digits of a number
//feb 17

import java.util.Scanner;

public class sumOfDigits
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int number, sum = 0, remainder;
        System.out.print("Enter a number: ");
        number = input.nextInt();
        while (number != 0)
        {
            remainder = number % 10;
            sum = sum + remainder;
            number = number / 10;
        }
        System.out.println("Sum of digits: " + sum);
    }
}