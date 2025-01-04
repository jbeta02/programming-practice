// LeetCode 27. Remove Element
// time: O(n)
// space: O(1)

class RemoveElement {
    public int removeElement(int[] nums, int val) {
        int moveI = 0;
        int currI = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == val) {
                currI += 1;
            }
            else {
                nums[moveI] = nums[i];
                moveI++;
            }
        }
        return moveI;
    }
}