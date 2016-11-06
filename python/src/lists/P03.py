'''
1.03 (*) Find the K'th element of a list.
    The first element in the list is number 1.
    Example:
    ?- element_at(X,[a,b,c,d,e],3).
    X = c
'''

class P03():
    def __init__(self):
        pass

    def get_kth_element(self, elements, position):
        if position-1 > len(elements):
            raise Exception("Value of position parameter must be less than length of array elements.")
        return elements[position]
