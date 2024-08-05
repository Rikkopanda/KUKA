import serial
import time
import sys
from enum import Enum

def calculate_checksum(values):
    return sum(values)

def open_serial_port():
    ser = serial.Serial(
        port,
        baudrate,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_EVEN,
        stopbits=serial.STOPBITS_ONE,
        xonxoff=True,
        timeout=0.5
    )
    return ser


class Index_val(Enum):
    X_I = 0
    Y_I = 1
    Z_I = 2
    A_I = 3
    B_I = 4
    C_I = 5
    DELAY_I = 6


def send_position_data(port, baudrate, positions):
    ser = open_serial_port()



    for position in positions:

        read_str = ser.read(30)
        print(f"read: {read_str.strip()}\n")

        # if read_str == "error":
        #     print(f"msg from kuka: {read_str.strip()}\n")
        x, y, z, a, b, c, s, t, delay = position
        checksum = calculate_checksum([x, y, z, a, b, c, s, t])
        data_str = f"{x} {y} {z} {a} {b} {c} {s} {t} {checksum}\n"


        input("Press Enter to send the next position...")
        ser.write(data_str.encode('utf-8'))
        print(f"Sent: {data_str.strip()}", file=sys.stdout)
        read_str = ser.read(30)
        print(f"read: {read_str.strip()}\n")
        # read_str = ser.read(30)
        # if read_str == "error":
        #     print(f"error msg from kuka received\n")
        # time.sleep(delay)
    ser.close()

if __name__ == "__main__":
    port = '/dev/ttyUSB0'  # Serial port to send data
    baudrate = 9600  # Baud rate
    delay = 2  # Time delay in seconds between sending data points
    
    # Example positions (x, y, z, a, b, c)
    positions = [
        (721, -216, 1413, 180, 9, -176, 2, 10, 5),
        (805, -216, 1326, 180, 9, -176, 2, 10, 5),
        (805, 79, 1335, 180, 9, -176, 2, 35, 5),
        (805, 79, 1413, 180, 9, -176, 2, 35, 5),

        # Add more positions as needed
    ]
        # "error msg from kuka received\n")
    send_position_data(port, baudrate, positions)
