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

## List Comprehensions

```python
# Squares of even numbers
squares = [x**2 for x in range(20) if x % 2 == 0]
print(squares)

# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5, 6]

# Dict comprehension
char_pos = {ch: i for i, ch in enumerate('abcde')}
print(char_pos)
```

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

## String Manipulation Basics

```python
s = 'hello world'

print(s.upper())         # HELLO WORLD
print(s.title())         # Hello World
print(s.split())         # ['hello', 'world']
print(s.replace('o', '0'))  # hell0 w0rld
print(s.count('l'))      # 3
print(s.find('world'))   # 6
```

String methods return new strings — strings are immutable in Python.
