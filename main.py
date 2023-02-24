from enum import Enum

from fastapi import FastAPI, File, UploadFile
import requests
import serial

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File()):
    with open('readme.gcode', 'w') as f:
        f.write(str(file))
    return {"file_size": len(file)}

def Upload_File():
   fle={'file': open('readme.gcode', 'rb'), 'filename': 'readme.gcode'}
   #url='http://localhost:5000/api/files/{}'.format('local')
   #payload={'select': 'true','print': 'false' }
   #header={'X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB' }
   #response = requests.post(url, files=fle,data=payload,headers=header)
   ser = serial.Serial('/dev/ttyACM0', 115200) # I've verified that this is the proper COM port, second argument is baud rate, which I actually wasn't all that sure of, but I tried both 115200 and 9600 since they are both pretty common. I didn't bother tuning any other COM port settings.
   ser.write(b'G28 X\n') # My second issue comes up when I'm not sure of the line ending character that the M2 expects (maybe \n, \r or even \r\n)
   ser.close()

if __name__=='__main__':
   Upload_File()
