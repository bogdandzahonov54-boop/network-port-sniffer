Version 2.0: Crash-Resilient Network Auditor

This version introduces robust error tracking and structured execution logging, transforming the script into a reliable security tool that gracefully handles network exceptions and manual interrupts.

What I learned here:

* **Low-Level Socket Auditing:** I mastered the `socket.connect_ex()` method, which safe-guards the loop by returning standard system error codes instead of crashing on closed ports.
* **Network Exception Mapping:** Wrapped the scanning engine in a `try-except` block to capture `socket.gaierror`. If the user inputs a broken hostname or an unresolvable IP address, the script catches it and reports clean diagnostics.
* **Signal Interrupt Capture:** Implemented graceful termination by intercepting `KeyboardInterrupt` (Ctrl+C). The script now exits cleanly upon manual intervention, utilizing the `\n` newline buffer to preserve console layout stability.
* **Standardized InfoSec Log Markers:** Adopted international logging conventions (`[+]` for open assets, `[!]` for errors, `[*]` for system status info) to align the command-line interface with professional penetration testing frameworks.


## How to run it:
1. Open your terminal in Linux or Windows.
2. Run the script: `python3 scan.py`
3. Input the target IP or hostname (e.g., `scanme.nmap.org`).
