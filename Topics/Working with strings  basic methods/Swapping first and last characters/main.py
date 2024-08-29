# This function takes a string as input and returns the string with the first and last characters swapped.
def swap_first_last(string):
    # Write your code here
    first_string= string[0] 
    last_string= string[-1]
    stripped = string.strip(first_string+last_string)
    return last_string + stripped + first_string
   


# Taking user's input
input_string = input()

# Invoking the function
result = swap_first_last(input_string)

# Printing the result
print(result)
