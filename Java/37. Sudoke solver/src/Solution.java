import java.util.*;
public class Solution {
	private static boolean isPosible(char[][] board, ArrayList<ArrayList<HashSet<Character>>> possibilities) {
		for (int i = 0; i < 9; ++i) {
			for (int j = 0; j < 9; ++j) {
				if (board[i][j] == '.' && possibilities.get(i).get(j).isEmpty()) return false;
			}
		}
		
		return true;
	}
	private static boolean isCompleat(char[][] board) {
		for (int i = 0; i < 9; ++i) {
			for (int j = 0; j < 9; ++j) {
				if (board[i][j] == '.') return false;
			}
		}
		
		return true;
	}
	private static void setDigit(char[][] board, ArrayList<ArrayList<HashSet<Character>>> possibilities, int i, int j, char digit) {
		board[i][j] = digit;
		for (int k = 0; k < 9; ++k) {
			possibilities.get(i).get(k).remove(digit);
			possibilities.get(k).get(j).remove(digit);
		}
		for(int n = 0; n < 3; ++n) {
			for (int m = 0; m < 3; ++m) {
				possibilities.get(i / 3 * 3 + n).get(j / 3 * 3 + m).remove(digit);
			}
		}
		
	}
	
	private static boolean fillAllUnambiguity(char[][] board){
        ArrayList<ArrayList<HashSet<Character>>> possibilities = new ArrayList<ArrayList<HashSet<Character>>>();
        for (int i = 0; i < 9; ++i) {
            possibilities.add(new ArrayList<HashSet<Character>>());
            for (int j = 0; j < 9; ++j) {
                possibilities.get(i).add(new HashSet<Character>());
                if (board[i][j] == '.')
                	for (Character k = '1'; k <= '9'; ++k) possibilities.get(i).get(j).add(k);
            }
        }
        for (int i = 0; i < 9; ++i) {
        	for (int j = 0; j < 9; ++j) {
        		if (possibilities.get(i).get(j).isEmpty()) {
        			setDigit(board, possibilities, i, j, board[i][j]);
        		}
        	}
        }
        boolean added = true;
        while (added) {
        	added = false;
        	for (int i = 0; i < 9; ++i) {
            	for (int j = 0; j < 9; ++j) {
            		if (possibilities.get(i).get(j).size() == 1) {
            			added = true;
            			setDigit(board, possibilities, i, j, possibilities.get(i).get(j).iterator().next());
            		}
            	}
            }
        }
        if (isCompleat(board)) return true;
        if (!isPosible(board, possibilities)) return false;
       
        for (int i = 0; i < 9; ++i) {
        	for (int j = 0; j < 9; ++j) {
        		if (!possibilities.get(i).get(j).isEmpty()) {
        			Iterator<Character> iter = possibilities.get(i).get(j).iterator();
        			while (iter.hasNext()) {
        				char[][] newBoard = new char[9][9];
        				for (int k = 0; k < 9; ++k) {
        					for (int n = 0; n < 9; ++n) {
        						newBoard[k][n] = board[k][n];
        					}
        				}
        				newBoard[i][j] = iter.next(); 
        				if (fillAllUnambiguity(newBoard)) {
        					for (int k = 0; k < 9; ++k) {
            					for (int n = 0; n < 9; ++n) {
            						board[k][n] = newBoard[k][n];
            					}
            				}
        					return true;
        				}
        			}
        		}
        	}
        }
        
        return false;
    }
    public static void solveSudoku(char[][] board) {
        fillAllUnambiguity(board);
    }

	public static void main(String[] args) {
		//char[][] board = {{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'}};
		char[][] board = {{'.','.','9','7','4','8','.','.','.'},{'7','.','.','.','.','.','.','.','.'},{'.','2','.','1','.','9','.','.','.'},{'.','.','7','.','.','.','2','4','.'},{'.','6','4','.','1','.','5','9','.'},{'.','9','8','.','.','.','3','.','.'},{'.','.','.','8','.','3','.','2','.'},{'.','.','.','.','.','.','.','.','6'},{'.','.','.','2','7','5','9','.','.'}};
		solveSudoku(board);
		for (int i = 0; i < 9; ++i) {
        	for (int j = 0; j < 9; ++j) {
        		System.out.print(board[i][j]);
        	}
        	System.out.println();
        }
	}

}
