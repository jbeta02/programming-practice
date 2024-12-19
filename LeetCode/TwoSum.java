// LeetCode 1. Two Sum

// time complexity: O(n^2)
// space complexity: O(1)

class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        
        // perform sum of the nums elements until target found or empty encountered (end of qualifed numbers list)
        for (int i = 0; i < nums.length; i++) {
            for (int j = nums.length - 1; j > i; j--) {
                // not needed since exactly one solution will be present
                // if (qualifiedNums[j] == null) {
                //     break;
                // }

                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }

        return new int[] {0, 0};
    }
}