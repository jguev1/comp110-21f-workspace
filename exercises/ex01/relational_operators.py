"""A program that uses input function to show how Python relational operators work"""

__author__ = "730328302"

left: str= input("Left-hand side: ")
right: str= input("Right-hand side: ")
int_left: int= int(left)
int_right: int= int(right)

is_less_than: str= str(bool(int_left < int_right))
is_at_least: str= str(bool(int_left >= int_right))
is_equal_to: str= str(bool(int_left == int_right))
is_not_equal: str= str(bool(int_left != int_right))

print(left + " < " + right + " is " +  is_less_than)
print(left + " >= " + right + " is " +  is_at_least)
print(left + " == " + right + " is " +  is_equal_to)
print(left + " != " + right + " is " +  is_not_equal)