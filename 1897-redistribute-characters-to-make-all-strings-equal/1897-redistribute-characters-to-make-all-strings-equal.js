/**
 * @param {string[]} words
 * @return {boolean}
 */
var makeEqual = function(words) {

    // Initialize an empty object to store character counts.
    let count = {};

    // Iterate through each word in the array.
    for (let element of words) {

        // Iterate through each character in the current word.
        for (let char of element) {
            
            // Update the count of the current character in the object.
            if (char in count) {
                count[char] += 1;
            } else {
                count[char] = 1;
            }
        }
    }

    // Get a list of all character occurrences.
    let count_list = Object.values(count);

    // Iterate through the counts and check if they are divisible by the number of words.
    for (let num of count_list) {
        // If the count is not divisible by the number of words, return false.
        if (num % words.length !== 0) {
            return false;
        }
    }

    // If all counts are divisible by the number of words, return true.
    return true;
};