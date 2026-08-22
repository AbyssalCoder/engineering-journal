## Palindrome — Two-pointer Approach

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

Runs in O(n/2) comparisons with O(1) extra space.

## File Handling in Python

```python
# Writing
with open('output.txt', 'w') as f:
    f.write('Hello, file!\n')
    f.write('Second line\n')

# Reading
with open('output.txt', 'r') as f:
    content = f.read()
    print(content)

# Reading line by line
with open('output.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

Always use `with` statements — they handle closing automatically.

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

## Selection Sort

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([29, 10, 14, 37, 13]))
```

Always O(n²) — not adaptive, but minimal swaps (n-1 at most).

## Factorial

```python
# Iterative
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Recursive
def factorial_rec(n):
    return 1 if n <= 1 else n * factorial_rec(n - 1)

print(factorial_iter(5))  # 120
```

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

## Reverse a Number

```python
def reverse_number(n):
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return reversed_n

print(reverse_number(12345))  # 54321
```

This uses modulus and integer division — no string conversion needed.

## Linear Search

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

nums = [4, 2, 7, 1, 9]
print(linear_search(nums, 7))  # 2
print(linear_search(nums, 5))  # -1
```

Time complexity: O(n). Works on unsorted arrays.
