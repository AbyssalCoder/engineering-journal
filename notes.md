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


<!-- updated examples -->

## Binary Search

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

sorted_arr = [1, 3, 5, 7, 9, 11]
print(binary_search(sorted_arr, 7))  # 3
```

Requires sorted input. Time complexity: O(log n).

## Binary Search

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

sorted_arr = [1, 3, 5, 7, 9, 11]
print(binary_search(sorted_arr, 7))  # 3
```

Requires sorted input. Time complexity: O(log n).


<!-- updated examples -->

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

## UDP — User Datagram Protocol

- **Connectionless** — no handshake
- **Unreliable** — no delivery guarantee
- **Fast** — minimal overhead

### Use cases
- Video streaming
- Online gaming
- DNS queries
- VoIP

### TCP vs UDP
| Feature      | TCP          | UDP          |
|-------------|-------------|-------------|
| Connection   | Yes          | No           |
| Reliability  | Guaranteed   | Best effort  |
| Speed        | Slower       | Faster       |
| Ordering     | Yes          | No           |

## Network Monitoring Commands

```bash
# Check connectivity
ping google.com

# Trace route to host
traceroute google.com   # Linux
tracert google.com      # Windows

# View active connections
netstat -tuln
ss -tuln                # modern alternative

# DNS lookup
nslookup example.com
dig example.com

# Capture packets
tcpdump -i eth0 port 80
```

## Docker Networking

### Network drivers
- **bridge** (default) — isolated network on host
- **host** — shares host's network stack
- **none** — no networking
- **overlay** — multi-host (Swarm)

```bash
docker network create mynet
docker run --network mynet --name app1 nginx
docker run --network mynet --name app2 alpine ping app1
```

Containers on the same user-defined bridge can resolve each other by name.


<!-- updated examples -->


<!-- indent fix -->

## UDP — User Datagram Protocol

- **Connectionless** — no handshake
- **Unreliable** — no delivery guarantee
- **Fast** — minimal overhead

### Use cases
- Video streaming
- Online gaming
- DNS queries
- VoIP

### TCP vs UDP
| Feature      | TCP          | UDP          |
|-------------|-------------|-------------|
| Connection   | Yes          | No           |
| Reliability  | Guaranteed   | Best effort  |
| Speed        | Slower       | Faster       |
| Ordering     | Yes          | No           |

## HTTPS & TLS

HTTPS = HTTP + TLS encryption.

### TLS handshake (simplified)
1. Client Hello (supported cipher suites)
2. Server Hello (chosen cipher + certificate)
3. Key exchange (asymmetric → symmetric key)
4. Encrypted communication begins

### Why HTTPS matters
- Encrypts data in transit
- Authenticates the server via certificates
- Prevents man-in-the-middle attacks
- Required for modern web features (service workers, geolocation)


