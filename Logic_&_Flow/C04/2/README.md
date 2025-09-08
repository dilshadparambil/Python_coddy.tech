# Add Contact

## Challenge

**Easy**

Now, create the `add_contact` function that takes one argument: `contact_book` (a dictionary). The function should:

1. Get input for the contact's name, phone, email, and address.
2. Check if the name already exists in the dictionary. If it does, print: `"Contact already exists!"`.
3. If not, save the contact in the following format:

```python
contact_book[name] = {
	"phone": phone,
	"email": email,
	"address": address
}
```

Then print: `"Contact added successfully!"`.

[Question](q.py) [solution](solution.py)