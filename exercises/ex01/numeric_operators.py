"""A program that uses input function to show how Python numeric operators work."""

__author__ = "730328302"

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
int_left: int = int(left)
int_right: int = int(right)
# exponents
int_result_exp: int = int_left**int_right
result_exp: str = str(int_result_exp)
# division
int_result_div: float = int_left/int_right
result_div: str = str(int_result_div)
# integer division aka id
int_result_id: int = int_left//int_right
result_id: str = str(int_result_id)
# remainder
int_result_rem: int = int_left%int_right
result_rem: str = str(int_result_rem)
# results
print(left + " ** " + right + " is " + result_exp)
print(left + " / " + right + " is " + result_div)
print(left + " // " + right + " is " + result_id)
print(left + " % " + right + " is " + result_rem)