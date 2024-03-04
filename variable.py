# variable : varible with single underscore(_), double underscore(__), tripe or more
class Variable:
    def __init__(self):
        self.local = 10    # public
        self._local = 20    # semi private should be as internal not public
        self.__local = 30    # private to class not public
        self.__local__ = 40    # private to class not public
        self.___local = 50     # private to class not public

vs = Variable()

print(vs.local)
print(vs._local)        # still accessed by object but should not use it as internal implementation may change without notice
# print(vs.__local)       # will return error AttributeError
# print(vs.__local__)     # will return error AttributeError

def change_counter(counter):

    def update_global_counter():
        global counter
        counter += 10

    def update_nonlocal_counter():
        nonlocal counter
        counter += 10

    def update_local_counter(counter):
        counter += 10

    # execution order
    update_global_counter() # counter : 20
    update_nonlocal_counter() # counter : 20
    update_local_counter(counter) # counter : 30

    # execution order
    update_local_counter(counter) # counter : 30
    update_nonlocal_counter() # counter : 20
    update_global_counter() # counter : 20

counter = 10
change_counter(counter)
print(counter) # counter : 20

