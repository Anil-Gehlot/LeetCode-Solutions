class Solution {
    public int maxSubArray(int[] nums) {

        //  to add all element of array
        int sum = 0;

        // to find the maximum sum 
        int max_sum = Integer.MIN_VALUE;

        // loop to iterate over the array
        for(int i=0; i<nums.length; i++){
            sum += nums[i];
            max_sum = Math.max(sum,max_sum);

            if (sum < 0){
                sum = 0;
            }
        }

        // to return maximum sum value.
        return max_sum;
    }
}