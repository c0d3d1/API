; ** FlashForge Creator Pro End Gcode by Reececache **
M73 P100 ; Turn off build progress
M140 S0 ; Stop heating bed
M104 S0 T0 ; Stop heating right extruder
M104 S0 T1 ; Stop heating left extruder
G1 Z145 F1200 ; Completely lower build plate
T0 ; Tell next job to use right extruder
G28 X Y F2500 ; Home X and Y axes
M18 ; Disable steppers
M70 P5 (Gcode by Reececache)
M72 P1 ; Play print complete song if sound is enabled