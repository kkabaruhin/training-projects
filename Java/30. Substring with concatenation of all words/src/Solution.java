import java.util.*;
public class Solution {

	static List<Integer> answer;
	static List<String> permutationList;
	static int n, wordLen;
    private static void permutation(String s, String[] words) {
        boolean[] isTaken = new boolean[n];
        for (int i = 0; i < n; ++i) isTaken[i] = false;
        permutation(s, "", words, isTaken, 0, n);
    }

    private static void permutation(String s, String prefix, String[] words, boolean[] isTaken, int del, int wordsLeft) {
    	int x = 0;
        if (prefix != "") {
        	x = s.indexOf(prefix.substring((n - wordsLeft - 1) * wordLen));
        }
        if (x == -1 || (x + (wordsLeft + 1) * wordLen) >= s.length()) return;
        if (wordsLeft == 0) {
        	int del2 = x;
        	int x1;
            while (x != -1) {
            	answer.add(del + del2);
                x1 = x;
                if (x + 1 + del2 >= s.length()) break;
                x = s.substring(x + 1 + del2).indexOf(prefix);
                del2 = del2 + 1 + x1 + x;
            }
        }
        else {
            for (int i = 0; i < n; i++)
            { 
                if (isTaken[i]) continue;
                boolean[] isTaken2 = new boolean[n];
                for (int j = 0; j < n; ++j) isTaken2[j] = isTaken[j];
                isTaken2[i] = true;
                permutation(s.substring(x), prefix + words[i], words, isTaken2, del + x, wordsLeft - 1);
            }
        }
    }

    public static List<Integer> findSubstring(String s, String[] words) {
        answer = new ArrayList<>();
        n = words.length;
        wordLen = words[0].length();
        permutation(s, words);
        answer.sort(null);
        List<Integer> newAnswer = new ArrayList<>();
        Integer prev = -1;
        for (Integer x: answer) {
        	if (x != prev) newAnswer.add(x);
        	prev = x;
        }
        return newAnswer;
    }

	public static void main(String[] args) {
		String s = "aaaaa";
		          //0123456789ABCDEFGH
		String[] words = {"a","a"};
		System.out.print(findSubstring(s, words));

	}

}
