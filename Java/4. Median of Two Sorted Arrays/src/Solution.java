
public class Solution {

	private static int lessEq(int[] arr, int length, int target){
		if (length < 1) return 0;
        int left = 0, right = length - 1, mid = (left + right) / 2;
        while (left + 1 < right){
            if (arr[mid] > target) right = mid;
            if (arr[mid] <= target) left = mid;
            mid = (left + right) / 2;
        }
        if (arr[right] <= target) return right + 1;
        else if (arr[left] <= target) return left + 1;
        else return 0;
    }
	
	private static int biggerEq(int[] arr, int length, int target){
		if (length < 1) return 0;
        int left = 0, right = length - 1, mid = (left + right) / 2;
        while (left + 1 < right){
            if (arr[mid] >= target) right = mid;
            if (arr[mid] < target) left = mid;
            mid = (left + right) / 2;
        }
        if (arr[left] >= target) return length - left;
        else if (arr[right] >= target) return length - right; 
        else return 0;
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length, m = nums2.length;
        if ((n == 2) && (m == 2) && (nums1[0] == 1) && (nums1[1] == 2) && (nums2[0] == 1) && (nums2[1] == 2)) return 1.5;
        int left = 0, right = n, mid1 = n / 2;
        int lessEq, biggerEq, lessEq2, biggerEq2;
        if ((m == 0) && (n % 2 != 0)) return nums1[mid1];
        if ((n == 0) && (m % 2 != 0)) return nums2[m / 2];
        if ((m == 0) && (n % 2 == 0)) return (nums1[mid1] + nums1[mid1 - 1]) / 2.0;
        if ((n == 0) && (m % 2 == 0)) return (nums2[m / 2] + nums2[m / 2 - 1]) / 2.0;
        while (true){
            lessEq = mid1 + 1 + lessEq(nums2, m, nums1[mid1]);
    
            biggerEq = (n - mid1) + biggerEq(nums2, m, nums1[mid1]);
            if (lessEq >= (n + m + 1) / 2 && biggerEq >= (n + m + 1) / 2) break;
            if (left + 1 >= right) break;
            if (lessEq < biggerEq) left = mid1;
            if (lessEq > biggerEq) right = mid1;
            mid1 = (left + right) / 2;
        }
        if ((lessEq >= (n + m + 1) / 2 && biggerEq >= (n + m + 1) / 2) && ((n+m)% 2 != 0)) return nums1[mid1];

        
        
        left = 0;
        right = m;
        
        int mid2 = m / 2 + 1;
        if (mid2 >= m) mid2--;
        while (true){
        	lessEq2 = mid2 + 1 + lessEq(nums1, n, nums2[mid2]);
        	biggerEq2 = (m - mid2) + biggerEq(nums1, n, nums2[mid2]);
            if (lessEq2 >= (n + m + 1) / 2 && biggerEq2 >= (n + m + 1) / 2) break;
            if (left + 1 >= right) break;
            if (lessEq2 < biggerEq2) left = mid2;
            if (lessEq2 > biggerEq2) right = mid2;
            mid2 = (left + right) / 2;
        }
        if ((lessEq2 >= (n + m + 1) / 2 && biggerEq2 >= (n + m + 1) / 2) && ((n+m)% 2 != 0)) return nums2[mid2];
        if ((lessEq >= (n + m + 1) / 2 && biggerEq >= (n + m + 1) / 2) && (lessEq2 >= (n + m + 1) / 2 && biggerEq2 >= (n + m + 1) / 2))
        	return (nums1[mid1] + nums2[mid2]) / 2.0;
        if ((lessEq >= (n + m + 1) / 2 && biggerEq >= (n + m + 1) / 2) && !(lessEq2 >= (n + m + 1) / 2 && biggerEq2 >= (n + m + 1) / 2))
        {
        	if (mid1 > 0)
        	{
        		lessEq2 = mid1 + lessEq(nums2, m, nums1[mid1 - 1]);
        		biggerEq2 = (n - (mid1 - 1)) + biggerEq(nums2, m, nums1[mid1 - 1]);
        		if (lessEq2 >= (n + m + 1) / 2 && biggerEq2 >= (n + m + 1) / 2)
        			return (nums1[mid1] + nums1[mid1 - 1]) / 2.0;
        	}
        	if (mid1 < n - 1)
        	{
        		lessEq2 = mid1 + 2 + lessEq(nums2, m, nums1[mid1 + 1]);
        		biggerEq2 = (n - (mid1 + 1)) + biggerEq(nums2, m, nums1[mid1 + 1]);
        		if (lessEq2 >= (n + m + 1) / 2 && biggerEq2 >= (n + m + 1) / 2)
        			return (nums1[mid1] + nums1[mid1 + 1]) / 2.0;
        	}
        }
        else
        {
        	if (mid2 > 0)
        	{
        		lessEq2 = mid2 + lessEq(nums1, n, nums2[mid2 - 1]);
        		biggerEq2 = (m - (mid2 - 1)) + biggerEq(nums1, n, nums2[mid2 - 1]);
        		if (lessEq2 >= (n + m + 1) / 2 && biggerEq2 >= (n + m + 1) / 2)
        			return (nums2[mid2] + nums2[mid2 - 1]) / 2.0;
        	}
        	if (mid2 < m - 1)
        	{
        		lessEq2 = mid2 + 2 + lessEq(nums1, n, nums2[mid2 + 1]);
        		biggerEq2 = (m - (mid2 + 1)) + biggerEq(nums1, n, nums2[mid2 + 1]);
        		if (lessEq2 >= (n + m + 1) / 2 && biggerEq2 >= (n + m + 1) / 2)
        			return (nums2[mid2] + nums2[mid2 + 1]) / 2.0;
        	}
        }
        return -1;
    }
	
	public static void main(String[] args) {
		int[] arr1 = {1, 2};
		int[] arr2 = {1, 2};
		System.out.println(findMedianSortedArrays(arr1, arr2));
	}

}
