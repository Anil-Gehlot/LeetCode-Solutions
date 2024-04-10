from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        # Sort the deck in ascending order
        deck.sort()
        
        # Create a list of indices representing positions in the deck
        indices = [i for i in range(len(deck))]
        
        # Initialize a list to hold the reordered deck
        reordered_deck = [0 for i in range(len(deck))]

        # Iterate through each card in the sorted deck
        for card in deck:
            
            # Determine the position where the current card will be placed in the reordered deck
            current_index = indices.pop(0)
            
            # Place the current card at the determined position in the reordered deck
            reordered_deck[current_index] = card

            # If there are still indices left in the list
            if indices:
                
                # Move the last index to the end of the list, simulating moving the last card to the bottom of the deck
                last_index = indices.pop(0)
                indices.append(last_index)
        
        # Return the reordered deck
        return reordered_deck
