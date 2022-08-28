file=input("enter filer name")

if file.endswith('.png'):
    print('its png file')

elif file.endswith('.jpg'):
    print ("this is jpg file")

elif file.endswith('.docx'):
    print("this is docx file")

elif file.endswith('.py') or file.endswith('.ipynb'):
    print('its a python file')


else:
        print("un identified dstroyed ur file")
