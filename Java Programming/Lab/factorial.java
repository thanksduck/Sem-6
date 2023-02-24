//feb 24
//this program is to find the factorial of a number

import java.util.Scanner;

public class factorial
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int number, factorial = 1;
        System.out.print("Enter a number: ");
        number = input.nextInt();
        for (int i = 1; i <= number; i++)
        {
            factorial = factorial * i;
        }
        System.out.println("Factorial of " + number + " is " + factorial);
    }
}