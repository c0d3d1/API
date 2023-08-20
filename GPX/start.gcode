M73 P0 

M140 S[bed0_temperature] T0 
M134 T0 ; Stabilize bed temperature
G130 X20 Y20 Z20 A20 B20 

M126 S[fan_speed_pwm]
M104 S[extruder0_temperature] T0 
M104 S[extruder1_temperature] T1 

M133 T0 
M133 T1 
G130 X127 Y127 Z40 A127 B127 
G162 X Y F3600 
G161 Z F1200 