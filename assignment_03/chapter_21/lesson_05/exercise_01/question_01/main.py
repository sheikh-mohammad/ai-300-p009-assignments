numbers : list[int] = [1, 2, 3, 4, 5]

squared_numbers : list[int] = [num ** 2 for num in numbers]

print(f"Numbers: {numbers}")
print(f"Squared Numbers: {squared_numbers}")