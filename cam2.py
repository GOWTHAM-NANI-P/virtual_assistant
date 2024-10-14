import cv2
cam=cv2.VideoCapture(0)
fc=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
def met():
    while True:
        _,img=cam.read()
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=fc.detectMultiScale(grey,1.5,4)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+w),(255,255,255),3)# ,(),(),color,tickness of frame
        cv2.imshow("____",img)
        if cv2.waitKey(1)==32:
            break
    cam.release()
    cv2.destroyAllWindows()  
