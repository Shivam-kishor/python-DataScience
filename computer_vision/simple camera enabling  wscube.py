import cv2
#enabling camera
video_cap=cv2.VideoCapture(0)
while True:

    #read images
    ret,video_data=video_cap.read()
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10)==ord("a"):
        break
video_cap.release()
