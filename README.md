# network-port-sniffer

Wassup! This is my second tool for my cybersecurity portfolio. It is a simple, lightweight network port scanner written in Python.

I wrote this script to scan a remote target and find open TCP ports. I successfully tested it locally in my Ubuntu VM on a real server (`scanme.nmap.org`).

## What I learned here:
* **The `socket` library:** I learned how to use low-level network connections in Python to talk to remote IP addresses.
* **The `.connect_ex()` method:** I used this method to scan ports. It returns `0` if the port is open, which is very useful for `if/else` logic.
* **Network timeouts:** At first, my script was too slow. I discovered the `s.settimeout(0.3)` method. It stops the loop from freezing on closed ports and makes the scan super fast.
* **Ethics and law:** I learned that you must only scan targets that you own or have official permission to test.

## How to run it:
1. Open your terminal in Linux or Windows.
2. Run the script: `python3 scan.py`
3. Input the target IP or hostname (e.g., `scanme.nmap.org`).
