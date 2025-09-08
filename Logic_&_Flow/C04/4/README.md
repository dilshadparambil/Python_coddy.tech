# Edit Contact

## Challenge

**Easy**

The next step is to create the `edit_contact` function. This function will allow users to update the details of an existing contact in the Contact Book.

**Your Task:**

1. Create a function named `edit_contact` that takes one argument: `contact_book` (a dictionary).
2. Get input for the contact's name that the user wants to edit.
3. Check if the name exists in the `contact_book`:
   * If it exists, prompt the user to input new values for the contact's phone, email, and address (**in that order!**).
   * If the user provides no input (presses Enter), keep the current value for that field (in this case the input will be an empty string, `''`).
   * Update the contact's information in the dictionary.
   * Print: `"Contact updated successfully!"`.
4. If the contact does not exist, print: `"Contact not found!"`.

**Remember: Only read inputs for phone, email, and address if the contact exists in the contact book. If the contact is not found, print the error message immediately without trying to read additional inputs.**

**Expected Behavior:**

For a `contact_book` containing:

```python
{"Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"}}
```

If the user enters:

```python
Alice
987-654-3210

456 Elm St
```

The updated `contact_book` should look like this:

```python
{"Alice": {"phone": "987-654-3210", "email": "alice@example.com", "address": "456 Elm St"}}
```

If the user enters a name that does not exist:

```python
Bob
```

The output should be:

```python
Contact not found!
```

[Question](q.py) [solution](solution.py)