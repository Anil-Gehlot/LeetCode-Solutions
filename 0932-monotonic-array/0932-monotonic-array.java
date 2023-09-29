class Solution {
    public boolean isMonotonic(int[] nums) {

        boolean monotone_inc = false;
        boolean monotone_dec = false;

        for( int i = 0; i < nums.length -1; i++){

            if (nums[i] < nums[i+1]){
                monotone_inc = true;
            }
            else if( nums[i] > nums[i+1]){
                monotone_dec = true;
            }

            if ((monotone_inc==true) && (monotone_dec == true)){
                return false;
            }

        }
        
        return true;
        
    }
}