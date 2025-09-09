import serial
import time

# Change COM3 → your Arduino COM port
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Allow Arduino to reset

def read_from_arduino():
    """Read sensor values from Arduino as CSV."""
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        return line
    return None

def send_to_arduino(command):
    """Send sorting command to Arduino (METAL/WET/DRY)."""
    arduino.write((command + "\n").encode('utf-8'))

print("Smart Waste Segregation System started...")

try:
    while True:
        data = read_from_arduino()
        if data:
            try:
                ir_val, moisture_val, metal_val = map(int, data.split(','))
                print(f"IR={ir_val}, Moisture={moisture_val}, Metal={metal_val}")

                # Decision logic
                if metal_val == 1:
                    print("Detected: METAL WASTE")
                    send_to_arduino("METAL")

                elif moisture_val < 500:  # Adjust threshold based on sensor
                    print("Detected: WET WASTE")
                    send_to_arduino("WET")

                elif ir_val == 1:
                    print("Detected: DRY WASTE")
                    send_to_arduino("DRY")

            except ValueError:
                print("Invalid data:", data)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program...")
    arduino.close()
