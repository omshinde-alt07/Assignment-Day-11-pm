## 1️⃣ Exact Prompt Used

```
Write a Python decorator called @retry(max_attempts=3, delay=1)
that automatically retries a function if it raises an exception,
with exponential backoff.
Then test the decorator with a function that fails 50% of the time
using random.random(). Also provide a short critical evaluation.
```

---

# 2️⃣ AI-Generated Code

```python
import time
import random
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            attempt = 0

            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    attempt += 1

                    if attempt == max_attempts:
                        print(f"Function failed after {max_attempts} attempts")
                        raise

                    wait_time = delay * (2 ** (attempt - 1))
                    print(f"Error: {e}. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)

        return wrapper
    return decorator


@retry(max_attempts=3, delay=1)
def unreliable_function():
    if random.random() < 0.5:
        raise ValueError("Random failure occurred")
    return "Success!"


for i in range(5):
    try:
        print(unreliable_function())
    except Exception as e:
        print("Final failure:", e)
```

---

# 3️⃣ Testing the Decorator

The decorator was tested using a function that fails **50% of the time**.

The test function:

```python
random.random()
```

generates a number between **0 and 1**.

If the value is less than **0.5**, the function raises an exception.

This simulates **unreliable operations**, such as:

* network requests
* database queries
* API calls

### Example Output

```
Error: Random failure occurred. Retrying in 1 seconds...
Error: Random failure occurred. Retrying in 2 seconds...
Success!

Error: Random failure occurred. Retrying in 1 seconds...
Success!
```

The retry delay follows **exponential backoff**:

| Attempt | Delay     |
| ------- | --------- |
| 1       | 1 second  |
| 2       | 2 seconds |
| 3       | 4 seconds |

---

# 4️⃣ Critical Evaluation (200 Words)

The retry decorator provides a reusable mechanism for handling transient failures in Python programs. By wrapping a function with the `@retry` decorator, the function automatically retries execution when an exception occurs. This pattern is commonly used in production systems where failures may be temporary, such as unstable network connections or API rate limits.

One strength of this implementation is the use of exponential backoff. Instead of retrying immediately, the delay increases after each failed attempt. This reduces system load and avoids overwhelming external services. The decorator also uses `functools.wraps`, which preserves the original function's metadata such as its name and docstring.

However, the implementation has some limitations. First, it catches the base `Exception` class, which may unintentionally retry on errors that should not be retried, such as programming bugs. A more robust design would allow specifying which exceptions should trigger retries. Second, the retry behavior is synchronous, meaning the program blocks during `time.sleep`. In asynchronous systems, an async-compatible version would be preferable.

Overall, the decorator demonstrates a practical and widely used resilience pattern. With additional improvements such as configurable exception types and logging support, it could be suitable for real-world production environments.
