import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver = ("127.0.0.1", 9999)

# Example messages
messages = [
    "Hi",           # length 2 -> ignored
    "Hello",        # length 5 -> ACK
    "Goodbye",      # length 7 -> ACK
    "Python",       # length 6 -> ignored
    "Networking"    # length 10 -> ignored
]

for msg in messages:
    sock.sendto(msg.encode(), receiver)
    print(f"Sent: '{msg}'")
    
    try:
        sock.settimeout(1)          # wait max 1 sec for ACK
        ack, _ = sock.recvfrom(1024)
        print(f"Received: {ack.decode()}")
    except:
        print("No ACK received (non-prime or lost)")
    
    time.sleep(0.5)
