# Exercise 2: Filtering with Comprehensions
# 1. Keep numbers greater than 5: From [2, 5, 7, 1, 9, 3], get [7, 9]

numbers : list[int] = [2, 5, 7, 1, 9, 3]

nums_greater_than_5 : list[int] = [num for num in numbers if num > 5]

print(f"Numbers: {numbers}")
print(f"Numbers Greater than Five: {nums_greater_than_5}")