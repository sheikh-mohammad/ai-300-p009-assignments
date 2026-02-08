# 2. Extract first letters: ['a', 'b', 'c'] from ['apple', 'banana', 'cherry']

fruits : list[str] = ['apple', 'banana', 'cherry']

first_letters : list[str] = [fruit[0] for fruit in fruits]

print(f"Fruits: {fruits}")
print(f"Extracted First Letters: {first_letters}")