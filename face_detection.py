import face_recognition
import cv2
import numpy as np

#step 1
# loading images and converting them to RGB format
img_david = face_recognition.load_image_file('./images/train.jpg')
img_david = cv2.cvtColor(img_david, cv2.COLOR_BGR2RGB)

img_test = face_recognition.load_image_file('./images/TP2-10603.Ri_-757200097.jpg')
img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)

#step 2
# extracting the face locations and encoding them,also drawing the rectangle around the face for visualization
face_loc = face_recognition.face_locations(img_david)[0]
face_loc1 = face_recognition.face_locations(img_test)[0]
encode_david = face_recognition.face_encodings(img_david)[0]
encode_test = face_recognition.face_encodings(img_test)[0]
cv2.rectangle(img_david, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)
cv2.rectangle(img_test, (face_loc1[3], face_loc1[0]), (face_loc1[1], face_loc1[2]), (255, 0, 255), 2)

#step 3
# comparing the faces and printing the result
results = face_recognition.compare_faces([encode_david], encode_test)
#the first attribute in compare_faces must be a list of the known faces and then we compare with a new encoding that either you or user provides
# finding distance between the faces or more like the distance between the face encodings
face_distance = face_recognition.face_distance([encode_david], encode_test)
#adding the distance between the faces and the verdict on the image
cv2.putText(img_test, f'{results[0]} {round(face_distance[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
#viewing the images
cv2.imshow('david', img_david)
cv2.imshow('test', img_test)
cv2.moveWindow('david', 10, 10)
cv2.moveWindow('test', 800, 10)
cv2.waitKey(0)

#optional printing the verdict and distance between the faces
print(results[0],face_distance[0])
