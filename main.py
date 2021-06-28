import cv2 as cv
import numpy as np
import dlib
from imutils import face_utils

cap = cv.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

active = 0
drowsy = 0
sleep = 0
status=""
color=(0,0,0)

def calc(X,Y):
	dis = np.linalg.norm(X - Y)
	return dis

def stat(a,b,c,d,e,f):
	vtl = calc(b,d) + calc(c,e)
	htl = calc(a,f)
	ratio = vtl/htl

	if(ratio>0.42 and ratio<=0.50):
		return 1
	elif(ratio>0.50):
		return 2
	else:
		return 0


while True:
    frame = cap.read()
    image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = detector(image)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        face_frame = frame.copy()
        cv.rectangle(face_frame, (x1, y1), (x2, y2), (255, 250, 205), 2.5)

        position = predictor(image, face)
        position = face_utils.shape_to_np(position)

        right_eye = stat(position[42],position[43], 
        	position[44], position[47], position[46], position[45])
        left_eye = stat(position[36],position[37], 
        	position[38], position[41], position[40], position[39])
        
        if(right_eye==1 or left_eye==1):
        	active=0
        	drowsy+=1
        	sleep=0
        	if(drowsy>6):
        		status="Drowsy!"
        		color = (0,0,255)

        elif(right_eye==0 or left_eye==0):
        	active=0
        	drowsy=0
        	sleep+=1
        	if(sleep>6):
        		status="SLEEPING!!!"
        		color = (255,0,0)

        else:
        	active+=1
        	drowsy=0
        	sleep=0
        	if(active>6):
        		status="Active!"
        		color = (0,255,0)
        	
        cv.putText(frame, status, (100,100), cv.FONT_HERSHEY_DUPLEX, 1.25, color,2.5)

        for n in range(0, 68):
        	(x,y) = position[n]
        	cv.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv.imshow("Frame", frame)
    cv.imshow("Detector Result", face_frame)
    key = cv.waitKey(1)
    if key == 27:
      	break
