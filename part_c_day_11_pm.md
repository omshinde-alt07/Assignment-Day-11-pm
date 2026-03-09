# Q1 — Conceptual

## Execution Flow of try / except / else / finally

Python uses these blocks to manage errors and ensure programs handle failures gracefully.

## 1. try

The `try` block contains code that **may raise an exception**.

* Python executes this block first.
* If no error occurs → the `else` block runs.
* If an error occurs → Python jumps to the matching `except` block.

---

## 2. except

The `except` block handles specific exceptions raised in the `try` block.

Example:

```python
except ValueError:
```

This block runs **only if a ValueError occurs**.

If multiple except blocks exist, Python selects the **first matching exception type**.

---

## 3. else

The `else` block executes **only when the try block completes successfully** (no exception).

It is used for code that should run **only if the try block worked correctly**.

---

## 4. finally

The `finally` block **always executes**, whether an exception occurred or not.

It is typically used for:

* closing files
* releasing resources
* cleanup operations

---

# Example Using All Four Blocks

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Invalid input. Please enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("Result is:", result)

finally:
    print("Execution finished.")
```

### Execution Possibilities

| Situation         | Blocks Executed        |
| ----------------- | ---------------------- |
| Valid input       | try → else → finally   |
| ValueError        | try → except → finally |
| ZeroDivisionError | try → except → finally |

---

## What Happens if an Exception Occurs Inside the else Block?

If an exception occurs inside `else`:

* It **is not handled by the earlier except blocks**
* Python searches for another exception handler outside the structure
* The `finally` block **still executes**

Example:

```python
try:
    x = 5
except Exception:
    print("Error in try")

else:
    print(10 / 0)

finally:
    print("Cleanup executed")
```

Output:

```
Cleanup executed
ZeroDivisionError
```

---

# Q2 — Coding

## Function: safe_json_load(filepath)

### Requirements

The function must:

* safely read a JSON file
* handle multiple exceptions
* log errors
* return parsed dictionary on success
* return None on failure

---

## Implementation

```python
import json
import logging

logging.basicConfig(
    filename="json_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def safe_json_load(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        return None

    except json.JSONDecodeError:
        logging.error(f"Invalid JSON format in file: {filepath}")
        return None

    except PermissionError:
        logging.error(f"Permission denied while accessing: {filepath}")
        return None

    else:
        return data
```

---

## Example Usage

```python
data = safe_json_load("data.json")

if data is None:
    print("Failed to load JSON file")
else:
    print("JSON loaded successfully")
```

---

# Q3 — Debug / Analyze

## Original Code

```python
def process_data(data_list):
    results = []
    for item in data_list:
        try:
            value = int(item)
            results.append(value * 2)
        except:
            print("Error occurred")
            continue
        finally:
            return results
    return results
```

---

# Problems in the Code

## 1. Bare except

The code uses:

```python
except:
```

This catches **every exception**, including:

* KeyboardInterrupt
* SystemExit

This is unsafe and hides real problems.

---

## 2. return inside finally

The `finally` block executes every loop iteration.

Because it contains:

```python
return results
```

the function exits **after the first iteration**, stopping the loop early.

---

## 3. Poor Error Message

The message:

```
Error occurred
```

does not indicate:

* which item failed
* why the error happened

This makes debugging difficult.

---

# Corrected Version

```python
def process_data(data_list):
    results = []

    for item in data_list:
        try:
            value = int(item)
            results.append(value * 2)

        except ValueError as e:
            print(f"Invalid value '{item}': {e}")
            continue

    return results
```

---

# Improvements Made

## Specific Exception Handling

Instead of a bare except, we now catch:

```python
except ValueError
```

This ensures that only **integer conversion errors** are handled.

---

## Removed return from finally

The loop now processes **all elements in the list** before returning results.

---

## Informative Error Message

The new error message shows:

* the problematic value
* the reason for failure

Example output:

```
Invalid value 'abc': invalid literal for int()
```

---

# Example

```python
data = ["10", "20", "abc", "40"]

print(process_data(data))
```

Output:

```
Invalid value 'abc': invalid literal for int() with base 10
[20, 40, 80]
```

---
