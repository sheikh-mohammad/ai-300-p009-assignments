# Exercise 4: Real-World Application
# You're building a contact management system. Create a dictionary for a contact with:
#   - name: "Alice Johnson"
#   - email: "alice@example.com"
#   - phone: "555-1234"
#   - age: 28
#   - verified: True (boolean)
# Access the contact's name and email. Then safely retrieve notes (which doesn't exist) with a default value of "No notes".

contact : dict[str, str | int | bool] = {
    "name" : "Alice Johnson",
    "email" : "alice@example.com",
    "phone" : "555-1234",
    "age" : 28,
    "verified" : True
}

print(f"Contact: {contact}")
print(f"Contact Name: {contact["name"]}")
print(f"Contact Email: {contact["email"]}")
print(f"Contact Notes: {contact.get("notes", "No notes")}")