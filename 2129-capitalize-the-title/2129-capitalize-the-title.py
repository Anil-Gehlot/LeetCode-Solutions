class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        # an empty string to store the capitalized title
        new_title = ""

        # Split the input title into words
        title = title.split()

        # Iterate over each word in the title
        for word in title:
            
            # Check if the length of the word is 1 or 2
            if len(word) <= 2:
                
                # If the length is 1 or 2, convert the word to lowercase and add it to the new title with a space
                new_title += word.lower() + " "
            else:
                # If the length is greater than 2, capitalize the word and add it to the new title with a space
                new_title += word.capitalize() + " "
        
        # Return the new title with leading and trailing spaces removed
        return new_title.rstrip()
