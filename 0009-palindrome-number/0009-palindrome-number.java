class Solution {
    public boolean isPalindrome(int x) {

        int num = x;
        int rev = 0;

        
        if(x<0){
            return false;
        }
        while(num!=0){
            int l_digit = num%10;
            rev = (rev*10) + l_digit;
            num = num/10;

        }
        if (x==rev){
            return true;
        }
        else{
            return false;
        }
    }
}