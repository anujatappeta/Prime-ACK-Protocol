import socket

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Setup UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 9999))
print("Prime-ACK Protocol Receiver running on port 9999...")

while True:
    data, addr = sock.recvfrom(1024)
    msg = data.decode()
    length = len(msg)
    
    if is_prime(length):        # <-- Unique PAP rule
        sock.sendto(f"ACK {length}".encode(), addr)
        print(f"ACK sent for prime-length message '{msg}' ({length})")
    else:
        print(f"Ignored non-prime message '{msg}' ({length})")
