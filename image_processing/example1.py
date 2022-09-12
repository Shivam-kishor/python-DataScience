#2 librabry for image processing
#computer vision librabry
#pillow library easy
from PIL import Image

im=Image.open('lin.jpg')#realtive addr
#im2=Image.open(r'C:\Users\Shiva\Pictures\Camera Roll\WIN_20220831_14_17_43_Pro.jpg')#absolute path

print(im)
#print(im2)


im.rotate(45).show()
#im2.rotate(30).show()