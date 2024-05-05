class Solution:

    # Method to calculate the discounted price
    def calculateDiscount(self, word, discount):
        try:
            # Extract the price from the word (ignoring the dollar sign)
            price = int(word[1:])
            
            # Calculate the discount in terms of currency value
            discount_price = (price * discount) / 100
            
            # Calculate the price after applying the discount
            price_after_discount = price - discount_price
            
            # Return the discounted price formatted with two decimal places
            return f"${format(price_after_discount, '.2f')}"
        
        except Exception as e:
            # If an error occurs, return the original word
            return word


    def discountPrices(self, sentence: str, discount: int) -> str:

        # Split the sentence into words
        sentence = sentence.split()

        # Variable to construct the new sentence with discounted prices
        new_sentence = ""

        # Iterate through each word in the sentence
        for word in sentence:
            # Check if the word starts with '$' and has more than one character
            if word[0] == "$" and len(word) > 1:
                # Calculate the discounted price
                discounted_price = self.calculateDiscount(word, discount)
           
                # Append the discounted price to the new sentence
                new_sentence += discounted_price + " "
            else:
                # If the word is not a price, append it as is
                new_sentence += word + " "
        
        # Return the new sentence, removing the trailing space
        return new_sentence.rstrip()
