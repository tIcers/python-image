from PIL import Image


mac = Image.open("example.jpg")

print(mac.size)

mac.crop((0,0,100,100))

pencil = Image.open('pencils.jpg')

print(pencil)

print(pencil.size)

x = 0
y = 0
w = 1950/3
h = 1300/10

pencil.crop((x,y,w,h))

half = 1993/2

x = half - 20
y = 800
w = half + 200
h = 1200

mac.crop((x,y,w,h))

mac_computer = mac.crop((x,y,w,h))
mac.paste(im=computer, box= (0,0))

print(mac)

mac.resize((3000,500))
rotated_mac = mac.rotate(90)