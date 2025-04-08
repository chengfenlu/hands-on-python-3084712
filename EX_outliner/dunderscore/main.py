class MyClass:
    def __init__(self):
        self.public_attribute = 10
        self._protected_attribute = 20 
         # Single underscore convention for protected
        self.__private_attribute = 30 
         # Double underscore for name mangling

    def get_private(self):
        return self.__private_attribute

obj = MyClass()
print(obj.public_attribute)        # Output: 10
print(obj._protected_attribute)     # Output: 20 (Accessing protected - generally discouraged)

# Trying to access the "private" attribute directly will raise an AttributeError
# print(obj.__private_attribute)   # Error: AttributeError: 'MyClass' object has no attribute '__private_attribute'

# Accessing the mangled attribute:
print(obj._MyClass__private_attribute)  # Output: 30 (Still accessible, but discouraged)
print(obj.get_private())              # Output: 30 (The intended way to access it)
