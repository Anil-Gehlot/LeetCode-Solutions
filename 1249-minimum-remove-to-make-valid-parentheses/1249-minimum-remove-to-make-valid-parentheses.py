class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # Convert the input string into a list of characters for easier manipulation
        characters = [char for char in s]
        stack = []  # Stack to keep track of the indices of opening parentheses
        
        # Iterate through the characters of the string
        for i in range(len(characters)):
            if characters[i] == "(":
                stack.append(i)  # Push the index of opening parenthesis onto the stack
                
            elif characters[i] == ")" and len(stack) == 0:
                characters[i] = ""  # If a closing parenthesis is encountered and the stack is empty, remove it
                
            elif characters[i] == ")":
                stack.pop()  # If a closing parenthesis is encountered and there is a matching opening parenthesis in the stack, pop it
        
        # Remove any unmatched opening parentheses by setting their corresponding positions to an empty string
        for index in stack:
            characters[index] = ""
        
        # Join the list of characters back into a string and return
        return "".join(characters)

        