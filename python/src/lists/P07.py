'''
1.07 (**) Flatten a nested list structure.
Transform a list, possibly holding lists as elements into a 'flat' list by replacing each list with its elements (recursively).

Example:
?- my_flatten([a, [b, [c, d], e]], X).
X = [a, b, c, d, e]

Hint: Use the predefined predicates is_list/1 and append/3
'''

class P07():
    def __init__(self):
        pass

    def get_flatten_array(self, elements):
        flattenArray = []
        for i in elements:
            if type(i) is list:
                subFlattenArray = self.get_flatten_array(i)
                flattenArray += subFlattenArray
            else:
                flattenArray.append(i)

        return flattenArray
