from PIL import Image
#im=
im2=Image.open(r'C:\Users\Shiva\Pictures\Camera Roll\WIN_20220831_14_17_43_Pro.jpg')


print('resolution',im2.size)
print('height',im2.height)
print('mode',im2.mode)
print('format',im2.format)
print('exif',im2.info)

#im2.convert('L').show()



#im2.resize((100,200)).show()


#im2.resize((9000,2000)).show()



im2.resize((im2.width*5,im2.height*5)).save('carrot_5x.jpg')