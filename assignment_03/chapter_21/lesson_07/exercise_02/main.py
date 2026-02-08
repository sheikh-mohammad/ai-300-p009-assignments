# Exercise 2: Safe Access with .get()
# Using the book dictionary from Exercise 1, safely access:
#   - publisher (doesn't exist) with default "Unknown Publisher"
#   - pages (exists) to get the actual value
#   - rating (doesn't exist) with default 0.0
# Print all three values.

book : dict[str, str | int] = {
    "title" : "The Pragmatic Programmer",
    "author" : "David Thomas",
    "year" : 1999,
    "pages" : 352
}

print(f"Book Dictionary: {book}")
print(f"Publisher: {book.get("publisher", "Unknown Publisher")}")
print(f"Pages: {book.get("pages")}")
print(f"Rating: {book.get("rating", 0.0)}")