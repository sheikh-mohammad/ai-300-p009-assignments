# Exercise 3: Transform and Filter
# 1. Square only odd numbers: From [1, 2, 3, 4, 5], get [1, 9, 25]

numbers : list[int] = [1, 2, 3, 4, 5]

odd_squared_nums : list[int] = [num ** 2 for num in numbers if num % 2 != 0]

print(f"Numbers: {numbers}")
print(f"Odd Squared Numbers: {odd_squared_nums}")