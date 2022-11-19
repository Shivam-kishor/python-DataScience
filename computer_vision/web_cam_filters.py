import cv2


def start_camera(cam_id=0):
    camera =cv2.VideoCapture(cam_id)
    while camera.isOpened():
        _ , image=camera.read()
        image2=image*255
        grey=cv2.cvtcolor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Web, Cam Output',image)
        cv2.imshow('Image 2',image2)
        cv2.imshow('Gray',gray)
        cv2.imshow('RGB',rgb)
        if cv2.waitKey(1) ==27: #escape keybr
            break

    camera.release()#free up the camera
    cv2.destroyAllWindows()# close all windows


    #starting of the lines
    start_camera(0)