import qrcode
from PIL import Image


data = "https://www.bilibili.com"
filename = "bilibili.png"
img = qrcode.make(data)
img.save(filename)