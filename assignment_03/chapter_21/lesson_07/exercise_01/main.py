# Exercise 1: Create a Typed Dictionary
# Create a dictionary representing a book with the following fields:
#   - title (string): "The Pragmatic Programmer"
#   - author (string): "David Thomas"
#   - year (integer): 1999
#   - pages (integer): 352
# Write the dictionary with proper type hints. Then print the title and author.

book : dict[str, str | int] = {
    "title" : "The Pragmatic Programmer",
    "author" : "David Thomas",
    "year" : 1999,
    "pages" : 352
}

print(f"Book Dictionary: {book}")
print(f"Title: {book["title"]}")
print(f"Author: {book["author"]}")