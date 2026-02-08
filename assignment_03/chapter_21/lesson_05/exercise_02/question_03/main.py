# Exercise 2: Filtering with Comprehensions
# 3. Keep only positive numbers: From [-5, 3, -1, 8, -2, 0, 6], get [3, 8, 6]

numbers : list[int] = [-5, 3, -1, 8, -2, 0, 6]

positive_numbers : list[int] = [num for num in numbers if num > 0]

print(f"Numbers: {numbers}")
print(f"Positive Numbers: {positive_numbers}")