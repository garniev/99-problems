'''
1.11 (*) Modified run-length encoding.
Modify the result of problem 1.10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as [N,E] terms.

Example:
?- encode_modified([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [[4,a],b,[2,c],[2,a],d,[4,e]]
'''

class P11():
    def __init__(self):
        pass

    def get_encoding_array_modified(self, elements):
        encodingArray = []
        elementArray = []
        lastItem = ''
        elementCounter = 0

        for i in elements:
            if i is not lastItem:
                elementCounter += 1
                elementArray = [0,i]
                encodingArray.append(elementArray)
            elementArray[0] +=1
            lastItem = i

        modifiedArray = []
        for i in encodingArray:
            if i[0] == 1:
                i = i[1]
            modifiedArray.append(i)

        return modifiedArray
