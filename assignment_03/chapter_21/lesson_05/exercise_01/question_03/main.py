# Exercise 1: Writing Simple Comprehensions
# 3. Convert to uppercase: ['HELLO', 'WORLD'] from ['hello', 'world']

lower_cased_words : list[str] = ['hello', 'world']

upper_cased_words : list[str] = [word.upper() for word in lower_cased_words]

print(f"Lower Cased Words: {lower_cased_words}")
print(f"Upper Cased Words: {upper_cased_words}")