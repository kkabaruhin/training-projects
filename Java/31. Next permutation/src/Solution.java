import java.util.Arrays;

public class Solution {
	
	public static void nextPermutation(int[] nums) {
        if (nums.length == 1) return;
        int leftIndex = nums.length - 2;
        while (leftIndex >= 0 && nums[leftIndex] >= nums[leftIndex + 1]) --leftIndex;
        if (leftIndex == -1) {
            Arrays.sort(nums);
            return;
        }
        int rightIndex = -1;
        for (int i = leftIndex + 1; i < nums.length; ++i){
            if (nums[i] > nums[leftIndex]) {
                if (rightIndex == -1 || nums[i] <= nums[rightIndex]) rightIndex = i;
            }
        }
        if (rightIndex == -1) return;
        int x = nums[leftIndex];
        nums[leftIndex] = nums[rightIndex];
        nums[rightIndex] = x;
        
        for (int i = leftIndex + 1; i < nums.length - 1; ++i){
            for (int j = leftIndex + 1; j < nums.length - 1; ++j) {
            	if (nums[j] > nums[j + 1]) {
                int y = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = y;
            	}
            }
        }
    }

	public static void main(String[] args) {
		int[] nums = {5,4,7,5,3,2};
		nextPermutation(nums);
		for (int i = 0; i < nums.length; ++i) {
			System.out.print(nums[i]);
		}
	}
}
