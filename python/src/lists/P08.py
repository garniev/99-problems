'''
1.08 (**) Eliminate consecutive duplicates of list elements.
If a list contains repeated elements they should be replaced with a single copy of the element. The order of the elements should not be changed.

Example:
?- compress([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [a,b,c,a,d,e]
'''

class P08():
    def __init__(self):
        pass

    def get_remove_duplicates(self, elements):
        noDuplicates = []
        for i in elements:
            if len(noDuplicates) == 0:
                noDuplicates.append(i)
            else:
                if i is not noDuplicates[-1]:
                    noDuplicates.append(i)
        return noDuplicates
