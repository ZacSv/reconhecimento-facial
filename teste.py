import cv2
import face_recognition as fr

imgElon = fr.load_image_file('123456.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
faceLoc = fr.face_locations(imgElon)[0]
cv2.rectangle(imgElon,(faceLoc[1],faceLoc[2]),(faceLoc[3],faceLoc[0]),(0,255,0),2)

encodeElon = fr.face_encodings(imgElon)[0]
cv2.imshow('Elon', imgElon)

cv2.waitKey(0)