# Simple TCP Port Scanner

A simple, educational port scanner written in Python.  
It uses a classic **TCP connect scan**: for each target port, it attempts to establish a TCP connection.  
If the connection succeeds, we assume the port is **open**.

---

## Features

- Scan a target host over a **custom port range**
- Maps common ports to their **well-known services** (22 → SSH, 80 → HTTP, …)
- **Optional, configurable timeout** per connection

---

## How it works (network side)

The scanner acts as a TCP **client**:
1. You specify a target IP/host and a range of ports.
2. For each port, the script tries to `connect()` using a TCP socket.
3. If the TCP 3-way handshake completes, the port is considered **open**.
4. If the connection is refused, times out, or is filtered by a firewall, the port is **not shown** (or considered closed/filtered).

This is the same logic used by many basic recon tools: *“if I can establish a TCP session, something is listening.”*

---

## Usage

```bash
python3 port_scanner.py --ip 127.0.0.1 --start 1 --end 1024 --timeout 0.5
```

### Saving results to a file

You can optionally write all **open** ports to a file using the `--output` flag.

```bash
python3 port_scanner.py --ip 127.0.0.1 --start 1 --end 1024 --output scan_results.txt


