import java.util.Scanner;

public class Palindrome {
    
    // Function to check if a string is a palindrome
    public static boolean isPalindrome(String str) {
        // Convert the string to lowercase to handle case insensitivity
        str = str.toLowerCase();
        
        // Initialize two pointers: one at the beginning and one at the end of the string
        int left = 0;
        int right = str.length() - 1;

        // Check characters from both ends of the string
        while (left < right) {
            // If characters don't match, it's not a palindrome
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++; // Move the left pointer forward
            right--; // Move the right pointer backward
        }
        return true; // If all characters match, it's a palindrome
    }

    public static void main(String[] args) {
        // Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);

        // Ask the user for a string input
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        
        // Check if the input is a palindrome
        if (isPalindrome(input)) {
            System.out.println("The string is a palindrome.");
        } else {
            System.out.println("The string is not a palindrome.");
        }

        // Close the scanner to avoid memory leaks
        scanner.close();
    }
}

