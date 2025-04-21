from pyzbar.pyzbar import decode
from PIL import Image

img=Image.open("1.png")

result=decode(img)

print(result)


