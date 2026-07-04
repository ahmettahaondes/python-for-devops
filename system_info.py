import platform
import socket

print("System Information")
print("-" * 30)
print(f"Operating System : {platform.system()}")
print(f"Release          : {platform.release()}")
print(f"Machine          : {platform.machine()}")
print(f"Processor        : {platform.processor()}")
print(f"Hostname         : {socket.gethostname()}")
