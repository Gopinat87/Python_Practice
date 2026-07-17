// to find palindrome

import java.util.Scanner;

public class palindrome {

    public static String isPalindrome(String text) {

        int left = 0;
        int right = text.length() - 1;

        while (left < right) {

            if (text.charAt(left) != text.charAt(right)) {
                return "Not a Palindrome";
            }

            left++;
            right--;
        }

        return "Palindrome";
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String word = sc.nextLine();

        System.out.println(isPalindrome(word));
    }
}