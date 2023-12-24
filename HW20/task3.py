
# How to find the length of a nested List in Python?
nested_list = ['apple', ['banana', 'cherry'], 'grape', ['elderberry', 'fig', 'pineapple']]

def total_elements(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += total_elements(i)
        else:
            total += 1
    return total

print(total_elements(nested_list))


