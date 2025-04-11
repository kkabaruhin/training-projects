
public class Solution {
	
	private static String multOnDigit(String num, char cdigit) {
        int digit = Character.getNumericValue(cdigit);
        StringBuilder answer = new StringBuilder("");
        int add = 0;
        for (int i = num.length() - 1; i >= 0; --i) {
            int digit2 = Character.getNumericValue(num.charAt(i));
            int mult = digit * digit2;
            mult = mult + add;
            answer.append(String.valueOf(mult % 10));
            add = mult / 10;
        }
        if (add != 0) answer.append(String.valueOf(add));
        answer.reverse();
        return answer.toString();
    }

    private static String multTen(String num, int count) {
        StringBuilder answer = new StringBuilder(num);
        for (int i = 0; i < count; ++i) answer.append("0"); 
        return answer.toString();
    }

    private static String sumTwoNum(String num1, String num2) {
        StringBuilder answer = new StringBuilder("");
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        boolean addOne = false;
        while (i >= 0 || j >= 0) {
            int digit1 = 0;
            if (i >= 0) digit1 = Character.getNumericValue(num1.charAt(i));
            int digit2 = 0;
            if (j >= 0) digit2 = Character.getNumericValue(num2.charAt(j));
            int digit3 = digit1 + digit2;
            if (addOne) ++digit3;
            answer.append(String.valueOf(digit3 % 10));

            addOne = digit3 > 9;
            --i;
            --j;
        }
        if (addOne) answer.append("1");
        answer.reverse();
        return answer.toString();
    }
    public static String multiply(String num1, String num2) {
    	if (num1.equals("0") || num2.equals("0")) return "0";
        String answer = "";
        int countZero = 0;
        for (int i = num2.length() - 1; i >= 0; --i) {
            String newNum = multOnDigit(num1, num2.charAt(i));
            newNum = multTen(newNum, countZero);
            answer = sumTwoNum(answer, newNum);
            ++countZero;
        }
        return answer;
    }

	public static void main(String[] args) {
		String num1 = "123456789";
		String num2 = "987654321";
		String answer = multiply(num1, num2);
		System.out.print(answer);

	}

}
