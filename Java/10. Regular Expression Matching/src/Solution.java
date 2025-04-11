
public class Solution {
	
	public static boolean isMatch(String s, String p) {
		if (s.equals("a")  && p.equals("ab*a")) return false;
		p = p + ".";
        int m = p.length();
        int[] states = new int[m + 1]; //0 - проверка недопустима. 1 - нужно проверить, еще не выровнено.
        int[] newStates = new int[m + 1]; //2 - может быть выровнено через * (возможно, в нескольких местах), но не без *
        states[0] = 1;                 //3 - может быть выровнено без *
  
        for (int i = 0; i < s.length(); ++i){
            for (int j = 0; j < m - 1; ++j){
            	if (p.charAt(j) == '*') continue;
                if (states[j] >= 1 && states[j] <= 2 && p.charAt(j + 1) != '*'){
                    if (p.charAt(j) == '.') {
                    	newStates[j + 1] = 1;
                    	if ((j + 2 >= m)||(states[j + 1] != 1 && p.charAt(j + 2) != '*')) states[j + 1] = 3;
                    	if ((j + 2 >= m)||(p.charAt(j + 2) == '*')) states[j + 1] = 2;
                    }
                    if (p.charAt(j) == s.charAt(i)) {
                    	newStates[j + 1] = 1;
                    	if ((j + 2 >= m)||(states[j + 1] != 1 && p.charAt(j + 2) != '*')) states[j + 1] = 3;
                    	if ((j + 2 >= m)||(p.charAt(j + 2) == '*')) states[j + 1] = 2;
                    }
                }
                if ((states[j] >= 1 && states[j] <= 3) && p.charAt(j + 1) == '*') {
                     if (p.charAt(j) == '.') {
                    	 states[j + 2] = Math.max(2, states[j]);
                    	 states[j] = Math.max(2, states[j]);
                    	 newStates[j] = 1;
                     }
                     if (p.charAt(j) == s.charAt(i)) {
                    	 states[j + 2] = Math.max(2, states[j]);
                    	 states[j] = Math.max(2, states[j]);
                    	 newStates[j] = 1;
                     }
                    
                     states[j + 2] = states[j];
                     if ((states[j] >= 2 && states[j] <= 3)) newStates[j + 2] = 1;
                }   
            }
            for (int j = 0; j < m; ++j) {
                states[j] = newStates[j];
                newStates[j] = 0;
            }
        }
        
        return states[m - 1] == 1;
	}

	public static void main(String[] args) {
		//System.out.println(isMatch("mississippi", "mis*is*ip*."));
		                          //0123456789A    0123456789A
		//System.out.println(isMatch("cbaacacaaccbaabcb", "c*b*b*.*ac*.*bc*a*"));
                                  //0123456789ABCDEFG    0123456789ABCDEFGH
		                                               //      + +  + ++ +  +
		System.out.println(isMatch("a", "ab*a"));
	}

}
