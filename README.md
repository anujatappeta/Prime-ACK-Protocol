# Prime-ACK Protocol (PAP)

**Prime-ACK Protocol (PAP)** is a lightweight, UDP-like communication protocol that **selectively acknowledges messages based on prime-length payloads**.  
It demonstrates how a simple rule (prime-length messages) can improve network efficiency and reliability over standard UDP.

---

## Features
- Works over **LAN/Wi-Fi** between two computers  
- Uses **UDP sockets** for fast, connectionless communication  
- **ACKs only prime-length messages**, ignoring others  
- Easy-to-understand Python implementation  
- Ideal for learning **network programming and protocols**  

---

## How to Run

To use PAP, first run the receiver on one computer. Open a terminal, navigate to the folder containing `receiver.py`, and run `python receiver.py`. The receiver will start listening on port 9999 and display:


On the sender computer, open `sender.py` and update the `receiver` variable with the IP address of the receiver computer and the same port 9999:

```python
receiver = ("<RECEIVER_IP>", 9999)
```
For example: "10.0.84.70". Then open a terminal in the sender folder and run python sender.py. The sender will send messages to the receiver, and display which messages were acknowledged:

