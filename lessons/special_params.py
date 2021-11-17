"""Examples of optional parameters and Union type parameters."""

from typing import Union

def hello(name: Union[str, int] = "World") -> str:
    """A delightful greeting function"""
    result: str = "Hello, "
    if isinstance(name,str):
        return result + name
    else:
        return result +"COMP" + str(name)

# Calling hello with an argument overrides the default value
print(hello("Jose"))
# Calling hello with no arguments leads to use of default value
print(hello())
print(hello(110))