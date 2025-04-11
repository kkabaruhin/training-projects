
public class Solution {
	
	public static String convert(String s, int numRows) {
        int n = s.length(), m;
        if (numRows <= 2) m = n;
        else m = (n / (numRows - 2)) * 2;
        if (m == 0) m = 1;
        char[][] strings = new char[numRows][m];
        int[] currNum = new int[numRows];
        for (int i = 0; i < numRows; ++i){
            currNum[i] = 0;
        }
        
        boolean state = false; //false == down, true == up
        int numberOfStr = 0;
        for (int i = 0; i < n; ++i){
            strings[numberOfStr][currNum[numberOfStr]] = s.charAt(i);
            ++currNum[numberOfStr];
            if (!state && numberOfStr == numRows - 1) state = true;
            else if (state && numberOfStr == 0) state = false;

            if (state) --numberOfStr;
            else ++numberOfStr;
            if (numRows == 1) numberOfStr = 0;
        }
        char[] answersChars = new char[n];
        int k = 0;
        for (int i = 0; i < numRows; ++i){
            for (int j = 0; j < currNum[i]; ++j){
                answersChars[k++] = strings[i][j];
            }
        }
        String answer = new String(answersChars);
        return answer;
    }

	public static void main(String[] args) {
		System.out.println(convert("PAYPALISHIRING", 7)); //PAHNAPLSIIGYIR

	}

}
