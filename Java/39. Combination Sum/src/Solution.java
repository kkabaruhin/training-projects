import java.util.*; 
public class Solution {
	
	public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<List<Integer>>> dinamicList = new ArrayList<List<List<Integer>>>();
        dinamicList.add(new ArrayList<List<Integer>>());
        for (int i = 1; i <= target; ++i){
            dinamicList.add(new ArrayList<List<Integer>>());
            for (int j = 0; j < candidates.length; ++j){
                if (i < candidates[j]) break;
                List<Integer> x = new ArrayList<Integer>();
                x.add(i);
                if (i == candidates[j]) dinamicList.get(i).add(x);
                for (List<Integer> elem: dinamicList.get(i - candidates[j])){
                    List<Integer> newElem = new ArrayList<Integer>(elem);
                    newElem.add(candidates[j]);
                    Collections.sort(newElem);
                    boolean isExist = false;
                    for (List<Integer> elem2: dinamicList.get(i)){
                        if (elem2.equals(newElem)){
                            isExist = true;
                            break;
                        }
                    }
                    if (!isExist)
                        dinamicList.get(i).add(newElem);
                }
            }
        }
        return dinamicList.get(target);
    }

	public static void main(String[] args) {
		int[] candidates = {2,3,6,7};
		int target = 7;
		List<List<Integer>> answer = combinationSum(candidates,target);
		for (List<Integer> elem: answer) {
			for (Integer i: elem) {
				System.out.print(i);
			}
			if (elem.isEmpty()) System.out.print(0);
			
			System.out.println();
		}
	}

}
