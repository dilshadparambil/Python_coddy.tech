# View Contact

## Challenge

**Medium**

Create a function named `view_contact` that displays details of a specific contact.

Your function should:

1. Take a contact book dictionary as input
2. Get a contact name from user input (using `input()`)
3. Display the contact's details if found
4. Print "Contact not found!" if the contact doesn't exist

When displaying a contact, use this exact format:

```python
Name: [name]
Phone: [phone]
Email: [email]
Address: [address]
```

Example:

If the contact book contains Alice's information and the user enters "Alice", output:

```python
Name: Alice
Phone: 123-456-7890
Email: alice@example.com
Address: 123 Main St
```

If the user enters "Bob" (who doesn't exist), output:

```python
Contact not found!
```

**Note:** Your function should only output the contact details or the error message - no additional prompting text.

[Question](q.py) [solution](solution.py)