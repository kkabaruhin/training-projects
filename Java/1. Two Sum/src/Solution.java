
public class Solution {
	/*private static void merge(int left, int mid, int right) {
	for (int i = left; i <= mid; i++) {
		arr_copy[i] = arr[i];
	}
	int i = left, j = mid + 1; 
	for (int k = left; k <= right; k++) {
		if (i > mid)
			arr[k] = arr[j++];
		else if (j > right)
			arr[k] = arr_copy[i++];
		else if (arr_copy[i] < arr[j])
			arr[k] = arr_copy[i++];
		else
			arr[k] = arr[j++];
	}
}*/
	private static int[] arr;
	
	private static void insertion_sort(int left, int right) {
		for (int i = left + 1; i <= right; i++) {
			int x = arr[i];
			for (int j = i - 1; j >= left && arr[j] > x; j--) {
				int y = arr[j];
				arr[j] = x;
				arr[j+1] = y;
			}
		}
	}
	
	private static void quick_sort(int left, int right) {
		int a, b, c, len, avg;
		len = right - left;
		a = (int) (Math.random() * len + left);
		b = (int) (Math.random() * len + left);
		c = (int) (Math.random() * len + left);
		avg = (a + b + c) / 3;
		//avg = left;
		int mid = arr[avg];
		int i = left, j = right;
		while (true) {
			while (i < j && arr[i] < mid) i++;
			while (i < j && arr[j] > mid) j--;
			if (i >= j) break;
			int x = arr[i];
			arr[i] = arr[j];
			arr[j] = x;
			i++;
			j--;
		}
		if (j - left > 10) quick_sort(left, j);
		else if (j != left) insertion_sort(left, j);
		
		if (right - j > 10) quick_sort(j + 1, right);
		else if (right != j) insertion_sort(j + 1, right);
	}
	
	private static int binary_search(int left, int right, int a) {
		int mid = (right + left) / 2;
		
		while (true) {
			if (arr[mid] < a) {
				
			}
		}
		
		return mid;
	}
	
	public static void main(String[] args) {
		int n = 4;
		arr = new int[n];
		arr[0] = 4;
		arr[1] = 2;
		arr[2] = 3;
		arr[3] = 1;
		quick_sort(0, n - 1);
		for (int i = 0; i < n; i++)
			System.out.println(arr[i]);
	}
}