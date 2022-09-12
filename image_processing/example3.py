from re import I
from PIL import Image,ImageFilter,ImageEnhance#<--------- 2 classes added
#im=#relative path

im2=Image.open(r'C:\Users\Shiva\Pictures\Camera Roll\WIN_20220831_14_17_43_Pro.jpg')#absolute path
im3=Image.open(r'C:\Users\Shiva\Documents\python DataScience\images\lin.jpg')#absolute path
#im2.filter(ImageFilter.EMBOSS).show()
#im2.filter(ImageFilter.CONTOUR).show()
#im2.filter(ImageFilter.FIND_EDGES).show()
#im2.filter(ImageFilter.BLUR).show()
#im2.filter(ImageFilter.SHARPEN).show()
#im2.filter(ImageFilter.SMOOTH).show()
#im2.filter(ImageFilter.MaxFilter).show(3)#whites
#im2.filter(ImageFilter.MinFilter).show(3)#blacks
#im2.filter(ImageFilter.MedianFilter).show(5)#greys
#im2.filter(ImageFilter.GaussianBlur).show(40)#greys

'''eim=ImageEnhance.Color(im2)
for i in range(0,10,2):
    eim.enhance(i).show()
    '''
imc=im2.copy()
im2_s=im3.resize((300,200))
imc.paste(im2_s,(0,400))
imc.show()