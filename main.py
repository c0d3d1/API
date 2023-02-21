from enum import Enum

from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File()):
    with open('readme.gcode', 'w') as f:
        f.write(str(file))
        r = requests.post('http://octopi.local/api/files/{file}')
    return {"file_size": len(file)}

def Upload_File():
   fle={'file': open('readme.gcode', 'rb'), 'filename': 'readme.gcode'}
   url='http://localhost:5000/api/files/{}'.format('local')
   payload={'select': 'true','print': 'false' }
   header={'X-Api-Key': 'FD550BD4DA2442BA906AD1850539D6DB' }
   response = requests.post(url, files=fle,data=payload,headers=header)
   print(response)

if __name__=='__main__':
   Upload_File()
