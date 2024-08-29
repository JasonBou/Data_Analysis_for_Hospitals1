#  You can experiment here, it won’t be checked

input_string = str(input())

def swap_first_last(string):
    new_string = string.replace("!", "")
    new_string = new_string.replace(",","")
    new_string = new_string.replace(".","")
    new_string = new_string.replace("?","")
    return new_string.lower()

print(swap_first_last(input_string))