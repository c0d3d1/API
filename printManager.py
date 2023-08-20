import serial
import re
import os
import time
from datetime import datetime

def open_serial_port(port_path):
    try:
        ser = serial.Serial(port=port_path, baudrate=115200)
        return ser
    except Exception as e:
        print(f"Error opening serial port {port_path}: {e}")
        return None

def command(ser, command):
  start_time = datetime.now()

  ser.write(str.encode(command)) 
  time.sleep(0.01)
  while True:
    print("looping")
    line = ser.readline()
    if line == b'ok\n':
      break

def printFile(fileSent, ser):
  with open(fileSent) as infile, open('output.gcode', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output
  file1 = open('output.gcode')
  Lines = file1.readlines()
 
  count = 0
  for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip().split(';')[0]))
    if line.startswith(';'):
      continue
    time.sleep(0.01)
    command(ser, line.strip().split(';')[0] + "\r\n")
    time.sleep(0.01)

def main():
    printer_config_file = "printerConfig.txt"
    with open(printer_config_file, 'r') as config:
        printer_lines = config.readlines()

    printer_ports = {}  # Dictionary to store printer names and their serial ports

    for line in printer_lines:
        match = re.match(r'^(.*?),(.*?),(.*?)$', line.strip())
        if match:
            printer_name = match.group(1)
            serial_port = match.group(3)
            printer_ports[printer_name] = serial_port

    open_serial_ports = {}  # Dictionary to store opened serial ports

    for printer_name, port_path in printer_ports.items():
        if os.path.exists(port_path):  # Check if serial port path exists
            ser = open_serial_port(port_path)
            if ser:
                open_serial_ports[printer_name] = ser
        else:
            print(f"Serial port path for {printer_name} does not exist: {port_path}")

    # Now you have a dictionary of opened serial ports for existing printers. You can use them to communicate.
    
    # For example:
    for printer_name, ser in open_serial_ports.items():
        printFile("testbenchy.gcode", ser)

        
    # Don't forget to close the serial ports when you're done:
    for ser in open_serial_ports.values():
        ser.close()

    

if __name__ == "__main__":
    main()