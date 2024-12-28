// LeetCode 26. Remove Duplicates from Sorted Array
// time: O(n)
// space: O(n)

import java.util.LinkedList;
import java.util.Queue;

class RemoveDuplicatesFromSortedArray {
    public int removeDuplicates(int[] nums) {
        int[] newNums = new int[nums.length];
        int uniqueNums = 0;
        int lastUniqueNum = 101;
        boolean hasBlank = false;
        Queue<Integer> blankIndex = new LinkedList<Integer>();

        for (int i = 0; i < nums.length; i++) {
            // if equal to last unique then curr is not unique
            if (nums[i] == lastUniqueNum) {
                nums[i] = 101;
                blankIndex.add(i);
                hasBlank = true;
            }
            else { // curr is unique
                lastUniqueNum = nums[i];
                if (hasBlank) {
                    nums[blankIndex.remove()] = nums[i];
                    nums[i] = 101;
                    blankIndex.add(i);
                    hasBlank = true;
                }
                uniqueNums++;
            }
        }

        return uniqueNums;
    }
}