// LeetCode 35. Search Insert Position
// time O(log n)
// space O(1)

public class SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
        int min = 0;
        int max = nums.length - 1;
        int index = (max + min) / 2;

        while (min != max) {

            if (target < nums[index]) {
                max = index - 1;

                if (max < 0) {
                    max = 0;
                }

                if (max < min) {
                    max = min;
                }
            }

            else if (target > nums[index]) {
                min = index + 1;

                if (min > nums.length - 1) {
                    min = nums.length - 1;
                }

                if (min > max) {
                    min = max;
                }
            }

            else {
                return index;
            }

            index = (max + min) / 2;
        }


        if (target < nums[index]) {
            return index;
        }

        else if (target > nums[index]) {
            index = index + 1;

            return index;
        }

        else {
            return index;
        }
    }
}
