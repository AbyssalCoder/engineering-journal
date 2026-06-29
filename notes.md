## Fibonacci Sequence

### Iterative approach

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

for i in range(10):
    print(fibonacci(i), end=' ')
# 0 1 1 2 3 5 8 13 21 34
```

**Key takeaway:** The iterative version runs in O(n) time and O(1) space.

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

## Aider — AI Pair Programming in Terminal

### Setup
```bash
pip install aider-chat
aider
```

### Features
- Works with GPT-4, Claude, local models
- Auto-commits changes with good messages
- `/add` files to context
- `/diff` to see pending changes
- Understands git history

Good for iterative development — it keeps track of conversation context.

## Cursor — AI-First Code Editor

Fork of VS Code with deep AI integration.

### Standout features
- Tab completion that understands context
- Cmd+K for inline edits
- Chat with codebase awareness
- Multi-file editing in one prompt

### Tips
- Use `.cursorrules` to set project conventions
- Reference files with `@filename` in chat
- Composer mode for multi-file changes

## Subnetting Basics

### CIDR notation
- `192.168.1.0/24` → 256 addresses, 254 usable hosts
- `10.0.0.0/8` → Class A, ~16 million hosts

### Quick subnet math
| CIDR | Subnet Mask     | Hosts |
|------|-----------------|-------|
| /24  | 255.255.255.0   | 254   |
| /25  | 255.255.255.128 | 126   |
| /26  | 255.255.255.192 | 62    |
| /27  | 255.255.255.224 | 30    |
| /28  | 255.255.255.240 | 14    |

Usable hosts = 2^(32 - prefix) - 2
