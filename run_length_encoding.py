# We choose a random string as input
input = 'AAABBBCCC'


# Run length encoding function that has as input the string defined above
def run_length_encoding(string):
    # We initialize the string variables
    encoded_string = ''
    prev_symbol = ''
    c = ''
    # We iterate through each symbol in the input string
    for symbol in string:
        if symbol != prev_symbol:
            # The iterator enters here if its value and the previous symbol are different
            if prev_symbol:
                # The encoded string saves how many continuous equal symbols there are and the value of these
                encoded_string += str(c) + prev_symbol
            # It sets the counter value to 1 to start again
            c = 1
            # And updates the new symbol
            prev_symbol = symbol
        else:
            # The iterator enters here if its value and the previous symbol are the same
            c += 1  # Sums the counter by 1
    encoded_string += str(c) + prev_symbol
    # Returns the encoded string containing how many consecutive equal symbols
    # there are + their value, for the whole string
    return encoded_string


# Calling the function and printing the encoded string
encoded_string = run_length_encoding(input)
print(encoded_string)
