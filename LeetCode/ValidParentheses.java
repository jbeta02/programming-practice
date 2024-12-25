// 20. Valid Parentheses
// time: O(n)
// space: O(n/2)

import java.util.Stack;

class ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();

        if (s.length() % 2 != 0) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            char curr = s.charAt(i);
            if (curr == '(' || curr == '[' || curr == '{') {
                stack.push(curr);
            }
            
            else if (curr == ')' || curr == ']' || curr == '}') {
                
                if (stack.isEmpty()) {
                    return false;
                }

                else if (curr == ')') {
                    if (stack.peek() == '('){
                        stack.pop();
                    }
                    else {
                        return false;
                    }
                }
                else if (curr == ']') {
                    if (stack.peek() == '['){
                        stack.pop();
                    }
                    else {
                        return false;
                    }
                }
                else if (curr == '}') {
                    if (stack.peek() == '{'){
                        stack.pop();
                    }
                    else {
                        return false;
                    }
                }
                else {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}