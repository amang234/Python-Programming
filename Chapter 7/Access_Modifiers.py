# Public Modifiers
class ABC:
    def __init__(self):
        self.public_attribute = 20 # This is a public attribute

    def public_function(): # this is a public function
        pass

obj1 = ABC()
print(obj1.public_attribute)


# Private Modifiers
class ABCD:
    def __init__(self):
        self.__private_attribute = 10 # This is a private attribute
    def __private_function(): # this is a private function
        pass

obj2 = ABCD()
print(obj2.__private_attribute)
obj2.__private_function()



# Protected Modifier
class ABCDE:
    def __init__(self):
        self._protected_attribute = 30 # This is a protected attribute
    def _protected_function(): # this is a protected function
        pass

obj3 = ABCDE()
print(obj3._protected_attribute)
obj3._protected_function()