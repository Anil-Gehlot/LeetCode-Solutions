class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        
        // Step 1: Sort the array in ascending order
        Arrays.sort(arr);
        
        // Step 2: Ensure the first element is 1, as it needs to be the minimum possible value
        if (arr[0] != 1) {
            arr[0] = 1;
        }
        
        // Step 3: Iterate through the array starting from the second element
        for (int i = 1; i < arr.length; i++){
            
            // Calculate the absolute difference between the current element and the previous one
            int difference = Math.abs(arr[i] - arr[i - 1]);
            
            // Step 4: If the difference is less than or equal to 1, no adjustment is needed
            if (difference <= 1){
                // Do nothing in this case
            } else {
                // Step 5: Adjust the current element to make the difference exactly 1
                // by adding 1 and subtracting the calculated difference
                arr[i] = arr[i] + 1 - difference;
            }
        }
        
        // Step 6: Return the maximum element in the modified array
        return arr[arr.length - 1];
    }
}
