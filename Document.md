# Error Handling Checklist

## Program 1 – Age Calculator

### Exceptions Caught
- ValueError

### Recovery Action
User is asked to enter the age again until valid input is provided.

### User Message
"Invalid input: Age must be between 0 and 150"

### Logging
No logging implemented.


---

## Program 2 – List Index Access

### Exceptions Caught
- ValueError
- IndexError

### Recovery Action
User must re-enter the index until it falls within the valid range.

### User Message
Invalid input for non-numeric entries.
Index range message for out-of-range indexes.

### Logging
No logging implemented.


---

## Program 3 – Dictionary Lookup with Logging

### Exceptions Caught
- ValueError
- KeyError

### Recovery Action
User is informed about the incorrect input or missing student name.

### User Message
"Student not found. Please check the name."

### Logging
Errors are logged to `error_log.txt`.

Logged Information:
- Timestamp
- Error type
- Error message
