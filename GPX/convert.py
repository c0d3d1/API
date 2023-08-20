import subprocess


input_file = 'start.gcode'
output_file = 'start.x3g'

subprocess.call(['gpx', input_file, "/dev/ttyACM0"])