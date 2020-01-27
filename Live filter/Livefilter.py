import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # the process of capturing video s basically capturing frames
    ret, frame = cap.read()

    # Our operations on the frame come here
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #GaussianBlur
    gray = cv2.GaussianBlur(img,(5,5),0)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
