import java.util.*;
public class Solution {
	
	private static String maxPalid(String s, int index, int length) {
		if (index == 0) return s.substring(0, 1);
		//if (index == length - 1) return s.substring(index, index + 1);
		int left = index - 1, right = index + 1;
		while (left >= 0 && right < length && s.charAt(left) == s.charAt(right)) {
			--left;
			++right;
		}
		
		int left2 = index - 1;
		int right2 = index;
		while (left2 >= 0 && right2 < length && s.charAt(left2) == s.charAt(right2)) {
			--left2;
			++right2;
		}
		
		if (right - left - 1 > right2 - left2 - 1) return s.substring(left + 1, right);
		else return s.substring(left2 + 1, right2);
	}

	public static String longestPalindrome(String s) {
		Queue<Integer> q = new ArrayDeque();
        int n = s.length();
		q.add(n/2);
		if (n/2 - 1 >= 0) q.add(n/2 - 1);
		
		String maxPalid = Character.toString(s.charAt(0));
		while (!q.isEmpty()) {
			int index = q.poll();
			String currPalid = maxPalid(s, index, n);
			if (currPalid.length() > maxPalid.length()) maxPalid = currPalid;
			
			
			if (index >= n - 1 || index <= 0) continue;
			if (index >= n/2) q.add(index + 1);
			else q.add(index - 1);
		}
		return maxPalid;
    }
	
	public static void main(String[] args) {
		System.out.print(longestPalindrome("ababba"));

	}

}
