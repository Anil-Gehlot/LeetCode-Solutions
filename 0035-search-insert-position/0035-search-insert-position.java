class Solution {
    public int searchInsert(int[] nums, int target) {
        
        // finding the index if target is present inside the nums
        for( int i = 0; i < nums.length; i++){
            if (nums[i] == target){
                return i;
            }
        }

        // finding a index where target shuold be placed
        for( int i = 0; i < nums.length; i++){
            if (nums[i] > target){
                return i;
            }
        }
        
        // target should be placed at the end 
        return nums.length;
    }
}