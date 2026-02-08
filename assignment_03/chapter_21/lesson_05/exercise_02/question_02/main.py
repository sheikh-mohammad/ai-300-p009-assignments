# Exercise 2: Filtering with Comprehensions
# 2. Keep strings longer than 3 characters: From ['it', 'hello', 'ok', 'python'], get ['hello', 'python']

strings : list[str] = ['it', 'hello', 'ok', 'python']

strings_3_chars : list[str] = [string for string in strings if len(string) > 3]

print(f"Strings: {strings}")
print(f"Strings Longer than 3 charcaters: {strings_3_chars}")