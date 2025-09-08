# List All

## Challenge

**Easy**

The next step is to create the `list_all_contacts` function. This function will allow users to view all the contacts stored in the Contact Book along with their details.

**Your Task:**

1. Create a function named `list_all_contacts` that takes one argument: `contact_book` (a dictionary).
2. Check if the `contact_book` is empty:
   * If it is empty, print: `"No contacts available."`.
3. If it is not empty:
   * Loop through each contact in the dictionary and print their name, phone, email, and address in a readable format.

**Expected Behavior:**

For a `contact_book` containing:

```python
{
    "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
    "Bob": {"phone": "234-567-8901", "email": "bob@example.com", "address": "456 Oak Ave"}
}
```

The output should be:

```python
Name: Alice
Phone: 123-456-7890
Email: alice@example.com
Address: 123 Main St

Name: Bob
Phone: 234-567-8901
Email: bob@example.com
Address: 456 Oak Ave
```

[Question](q.py) [solution](solution.py)