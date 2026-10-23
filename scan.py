import socket

ip_address = str(input("Input IP address: "))

for port_number in range(1, 100):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    result = s.connect_ex((ip_address, port_number))
    s.close()
    
    if result == 0:
        print(f"{port_number} is open")

print("Scanning finished.")
