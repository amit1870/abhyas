class Variable:
    def __init__(self):
        self.local = 10    # public
        self._local = 20    # semi private should be as internal not public
        self.__local = 30    # private to class not public
        self.__local__ = 40    # private to class not public

vs = Variable()

print(vs.local)
print(vs._local)        # still accessed by object but should not use it as internal implementation may change without notice
# print(vs.__local)       # will return error AttributeError
# print(vs.__local__)     # will return error AttributeError
