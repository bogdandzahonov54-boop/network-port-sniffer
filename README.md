Version 2.2: Global Scope Exception Handling

This release fixes a minor structural vulnerability by moving the core try block to the absolute top of the application. The scripting lifecycle is now fully encapsulated and protected from raw tracebacks under any runtime circumstances.
What I learned here:
• Global Exception Architecture: By moving the try: block immediately below the imports, I expanded the protective scope to encapsulate the user input routine itself. The application is now fully bulletproofed against unexpected terminations at any stage.
• Input Stage Protection: I discovered that throwing a manual interrupt (Ctrl+C) during the input() phase bypasses regular internal loop handlers. Implementing global scope monitoring ensures KeyboardInterrupt is trapped even before the first variable is defined.
• Strict Output Layout Formatting: Replaced standard text buffers with the explicit escaped newline character \n. This ensures that if an operator manually terminates the scan at the prompt interface, the terminal output preserves structural integrity and drops onto a fresh, readable line.
• Production-Ready Shell Design: Refined the overall syntax alignment to eliminate uncaught raw Python traceback screens, providing a clean, industry-standard console user experience (UX) suitable for professional tools.


## How to run it:
1. Open your terminal in Linux or Windows.
2. Run the script: `python3 scan.py`
3. Input the target IP or hostname (e.g., `scanme.nmap.org`).
