/**
 * @param {string} s
 * @return {number}
 */
var maxLengthBetweenEqualCharacters = function(s) {
    
    // Initialize the result to -1
    let result = -1;

    // Iterate through the string
    for (let i = 0; i < s.length - 1; i++) {
        
        for (let j = i + 1; j < s.length; j++) {
            
            // Check if characters at positions i and j are equal
            if (s[i] === s[j]) {
                
                // Calculate the length of the substring between the equal characters
                let diff = j - i - 1;

                // Update the result with the maximum length found so far
                result = Math.max(result, diff);
            }
        }
    }

    // Return the maximum length found, or -1 if no such substring exists
    return result;
};