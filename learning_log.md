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

## 2026-06-20

Revisited DNS Resolution and took better notes.

Connecting this to what I learned last week about related concepts.

## 2026-06-23

Went through Selection Sort concepts and examples.

Still need to work on the implementation details.

## 2026-06-29

Went through Windsurf concepts and examples.

Connecting this to what I learned last week about related concepts.

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

## Git Rebase

Rebase replays your commits on top of another branch.

```bash
git checkout feature
git rebase main
```

### Merge vs Rebase
| Merge                  | Rebase                  |
|------------------------|-------------------------|
| Creates merge commit   | Linear history          |
| Preserves history      | Rewrites commit hashes  |
| Safe for shared branch | Only for local branches |

**Golden rule:** Never rebase commits that have been pushed to a shared branch.

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
