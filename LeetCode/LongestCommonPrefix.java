// time: O(n) if n len of strs, O(n) if n len of strs[i]
// space: O(1) if n len of strs, O(n) if n len of strs[i]

public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        String compare = strs[0];
        String compareNext = "";
        int lastIndex = 0;

        for (int i = 0; i < strs.length - 1; i++) {
            compare = strs[i];
            compareNext = strs[i+1];
            // check if lengths are different, then adjust if needed
            if (compare.length() > compareNext.length()) {
                compare = compare.substring(0, compareNext.length());
            }

            else if (compare.length() < compareNext.length()) {
                compareNext = compareNext.substring(0, compare.length());
            }

            else {
                // no adjustment needed
            }

            lastIndex = compare.length();

            // compare strings
            for (;lastIndex >= 0; lastIndex--) {
                if (compare.equals(compareNext)) {
                    break;
                }
                compare = compare.substring(0, lastIndex);
                compareNext = compareNext.substring(0, lastIndex);
            }
            strs[i+1] = compare;
        }
        return compare;
    }
}
