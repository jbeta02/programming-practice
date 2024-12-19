// LeetCode 9. Palindrome Number
// time: O(n)
// space: O(n)

import java.util.ArrayList;
import java.lang.Integer;
import java.util.Stack;

class PalindromeNumber{
    public boolean isPalindrome(int x) {

        // if neg return false
        if (x < 0) {
            return false;
        }

        // move int digits to array
        ArrayList<Integer> digits = new ArrayList<Integer>();

        if (x == 0) {
            digits.add(x);
        }

        while (x != 0) {
            digits.add(x % 10);
            x /= 10; // remove right digit from int since added to list
        }

        // len 0 and 1 cases
        if (digits.size() == 0 || digits.size() == 1) {
            return true;
        }

        int halfIndex;
        if (digits.size() % 2 == 0) {
            halfIndex = (digits.size() / 2) - 1; // integer division
        }
        else {
            halfIndex = (digits.size() / 2); // integer division
        }

        Stack<Integer> stack = new Stack<Integer>();
        boolean firstPop = false;

        for (int i = 0; i < digits.size(); i++) {
            if (i <= halfIndex) {
                stack.push(digits.get(i));
            }

            else{
                if (digits.size() % 2 != 0 && firstPop == false) { // if len not even
                    stack.pop();
                    firstPop = true;
                }

                if (!stack.empty()) {
                    if (digits.get(i) != stack.pop()) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}