
public class Solution {

	private static boolean isOk(String[] strs, int left, int right){
        for (int j = left; j <= right; ++j){
            char c = strs[0].charAt(j);
            for (int i = 1; i < strs.length; ++i){
                if (strs[i].charAt(j) != c) return false;
            }
        }
        return true;
    }
    public static String longestCommonPrefix(String[] strs) {
        int left = 0, right = 300;
        for (int i = 0; i < strs.length; ++i) if (strs[i].length() < right) right = strs[i].length();
        if (right == 0) return "";
        right -= 1;
        while (right > left + 1){
            int mid = (left + right) / 2;
            if (isOk(strs, left, mid)) left = mid;
            else right = mid;
        }
        if (isOk(strs, left, right)) return strs[0].substring(0, right + 1);
        if (left == 0) {
            char c = strs[0].charAt(0);
            for (int i = 1; i < strs.length; ++i){
                if (strs[i].charAt(0) != c) return "";
            }
            return strs[0].substring(0, 1);
        }
        return strs[0].substring(0, left + 1);
    }
    
    public static void main(String[] args) {
    	String[] arg = {"flower","flow","flight"};
    	System.out.println(longestCommonPrefix(arg));
    }

}
