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
