import ctypes
import requests
import os

ptp = os.environ['appdata']
imgfn = "wlp.jpg"
phhhh = f"{ptp}{os.sep}{imgfn}"
respuesta = requests.get("https://i.ibb.co/JKq3LQJ/infectado.jpg")
file = open(phhhh, "wb")
file.write(respuesta.content)
file.close()
ctypes.windll.user32.SystemParametersInfoW(20, 0, phhhh , 0)