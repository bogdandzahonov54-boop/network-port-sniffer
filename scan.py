import socket

try:
    ip_address = str(input("Input IP address: "))
    for port_number in range(1, 100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip_address, port_number))
        s.close()
        if result == 0:
            print(f"{port_number} is open")
except socket.gaierror:
    print("[!] Error: Invalid IP adress or hostname.")
except KeyboardInterrupt:
    print("\n[*] Scanning interrupted by user.")
print("Scanning finished.")

