import re

def get_max_page_vinmec(input_string):
    # Extract only integers using regular expressions
    integers = re.findall(r'\d+', input_string)

    # Convert the list of strings to integers
    integers = [int(num) for num in integers]
    
    return max(integers)