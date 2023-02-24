//this is a program to tell whether a number is palindrome or not
//feb 24
import java.util.Scanner;
public class isPalindrome
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int number, reverse = 0, remainder;
        System.out.print("Enter a number: ");
        number = input.nextInt();
        int temp = number;
        while (number != 0)
        {
            remainder = number % 10;
            reverse = reverse * 10 + remainder;
            number = number / 10;
        }
        if (temp == reverse)
        {
            System.out.println("The number is a palindrome");
        }
        else
        {
            System.out.println("The number is not a palindrome");
        }
    }
}