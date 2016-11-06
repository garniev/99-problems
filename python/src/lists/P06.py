'''
1.06 (*) Find out whether a list is a palindrome.
A palindrome can be read forward or backward; e.g. [x,a,m,a,x].
'''

class P06():
    def __init__(self):
        pass

    def is_palindrome(self, elements):
        backupList = []
        for i in elements:
            backupList.append(i)
        backupList.reverse()
        return backupList == elements
