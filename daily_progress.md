## Exception Handling

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Cannot divide by zero!')
        return None
    except TypeError as e:
        print(f'Type error: {e}')
        return None
    finally:
        print('Division attempted.')

print(safe_divide(10, 3))
print(safe_divide(10, 0))
```

`finally` always runs — useful for cleanup.

## Star Pattern — Right Triangle

```python
n = 5
for i in range(1, n + 1):
    print('* ' * i)
```

Output:
```
* 
* * 
* * * 
* * * * 
* * * * * 
```

## 2026-07-02

Deep dive into Subnetting Basics.

Going to revisit this topic next week for deeper understanding.


<!-- formatting -->

## Python Dictionary Practice

```python
# Word frequency counter
text = 'the cat sat on the mat the cat'
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)  # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

# Using collections.Counter
from collections import Counter
print(Counter(text.split()))
```

## 2026-07-15

Went through Dictionary Practice concepts and examples.

Connecting this to what I learned last week about related concepts.
