#from tkinter.tix import IMAGE
from PIL import Image,ImageDraw,ImageFont #<---------------these class help to draw on image

#im=#relative address
im2=Image.open(r'C:\Users\Shiva\Documents\python DataScience\images\lin.jpg')
im3=Image.open(r'C:\Users\Shiva\Documents\python DataScience\images\lin.jpg')#absolute path

font=ImageFont.truetype(r'C:\Users\Shiva\AppData\Local\Microsoft\Windows\Fonts\I Like it BOLD - TTF.ttf',140)
font2=ImageFont.truetype(r'C:\Users\Shiva\AppData\Local\Microsoft\Windows\Fonts\I Like it BOLD - TTF.ttf',40)

imd=ImageDraw.Draw(im2)

imd.text((200,100),'carrots',fill=(250,150,0),font=font)
imd.text((700,700),'$$',fill=(0,0,0),font=font2)


im2.save('edited_carrot.jpg')