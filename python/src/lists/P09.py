'''
1.09 (**) Pack consecutive duplicates of list elements into sublists.
If a list contains repeated elements they should be placed in separate sublists.

Example:
?- pack([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [[a,a,a,a],[b],[c,c],[a,a],[d],[e,e,e,e]]
'''

class P09():
    def __init__(self):
        pass

    def get_packed_array(self, elements):
        packedArray = []
        elementArray = []
        lastItem = ''

        for i in elements:
            if i is not lastItem:
                elementArray = []
                packedArray.append(elementArray)
            elementArray.append(i)
            lastItem = i

        return packedArray
