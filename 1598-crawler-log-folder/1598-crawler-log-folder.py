class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        # a variable to keep track of the moves
        move = 0

        # Iterate through each operation in the logs
        for operation in logs:
            
            # If the operation is to move to the parent folder ("../")
            if operation == "../":
                
                # Decrement the move variable by 1 if it's greater than 0
                move -= 1 if move > 0 else 0
                
            # If the operation is to remain in the same folder ("./"), do nothing
            elif operation == "./":
                pass
            
            # If the operation is to move to a child folder ("x/"), increment the move variable by 1
            else:
                move += 1
        
        # Return the final value of the move variable, representing the minimum number of operations
        return move
