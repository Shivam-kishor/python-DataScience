
import cv2 #alwasy write cv2 this not version

"""

camera=cv2.VideoCapture(0)
while camera.isOpened():
    status,image=camera.read()

    
    print(status,image.shape) #VGR✅ is foloowimg order Not RGB❌ red green blue
    
    #    (480,640,3)
    # height ,Width it show ,VGR
    
    """



"""
#camera open

camera=cv2.VideoCapture(0) 
while camera.isOpened():
    status,image=camera.read()

    cv2.imshow('Web Cam Output',image)
    if cv2.waitKey(1)== 27:   #27 means excape button
        break
    camera.release() #free up the camera 
    cv2.destroyAllWindows()#close all windows   

"""


def start_camera(cam_id=0):
    camera =cv2.VideoCapture(cam_id)
    while camera.isOpened():
        _,image=camera.read()
        cv2.imshow('Web, Cam Output',image)
        cv2.imshow('Image 2', image2)
        cv2.imshow('Gray',image)
        cv2.imshow('RGB', rgb)
        if cv2.waitKey(1) ==27: #escape keybr
            break

    camera.release()#free up the camera
    cv2.destroyAllWindows()# close all windows
    
    #double undescore __name__ is a special variable
    if __name__=='__main__':
        start_camera(0)#0 s is the defualt camera
