class Solution {
    public boolean isPowerOfTwo(int n) {

        // to return False for negative values
        if ( n <= 0 ){
            return false;
        }

        while( n%2 == 0 ){
            n = n/2;
        }

        if ( n == 1 ){
            return true;
        }
        else{
            return false;
        }

        
    }
}