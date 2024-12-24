// LeetCode 13. Roman to Integer
// Time: O(n)
// Space: O(1)

import java.util.HashMap;

class RomanToInteger {
    public int romanToInt(String s) {
        HashMap<Character, Integer> romanMapping = new HashMap<Character, Integer>();

        romanMapping.put('I', 1);
        romanMapping.put('V', 5);
        romanMapping.put('X', 10);
        romanMapping.put('L', 50);
        romanMapping.put('C', 100);
        romanMapping.put('D', 500);
        romanMapping.put('M', 1000);

        char curr;
        char next;
        int total = 0;

        for (int i = 0; i < s.length(); i++) {

            curr = s.charAt(i);

            if (i + 1 > s.length() - 1) {
                total += romanMapping.get(curr);
                break;
            }

            next = s.charAt(i + 1);

            if (romanMapping.get(curr) < romanMapping.get(next)){
                total -= romanMapping.get(curr);
            }

            else {
                total += romanMapping.get(curr);
            }
            
        }

        return total;
    }
}