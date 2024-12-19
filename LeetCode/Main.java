

public class Main {

    public static void main(String[] args) {
        TwoSum twoSum = new TwoSum();
        int[] list = twoSum.twoSum(new int[]{3, 2, 4}, 5);

        System.out.println(list[0] + " " + list[1]);
    }
}