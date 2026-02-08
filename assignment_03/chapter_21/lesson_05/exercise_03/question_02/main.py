# Exercise 3: Transform and Filter
# 2. Uppercase only words longer than 4 characters: From ['hi', 'hello', 'hey', 'python'], get ['HELLO', 'PYTHON']

words : list[str] = ['hi', 'hello', 'hey', 'python']

upper_cased_words : list[str] = [word.upper() for word in words if len(word) > 4]

print(f"Words: {words}")
print(f"Uppercase only words longer than 4 characters: {upper_cased_words}")