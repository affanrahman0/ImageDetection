# Importing all required packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read in the cascade classifiers for face and eyes
face_cascade = cv2.CascadeClassifier('venv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
#eye_cascade = cv2.CascadeClassifier('../DATA / haarcascades / haarcascade_eye.xml')


# create a function to detect face
def adjusted_detect_face(img):
    face_img = img.copy()

    face_rect = face_cascade.detectMultiScale(face_img,
                                              scaleFactor=1.2,
                                              minNeighbors=5)
    length = len(face_rect)
    if length==0:
        print('face not detected')


    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)
    return face_img


# create a function to detect eyes
# def detect_eyes(img):
#     eye_img = img.copy()
#     eye_rect = eye_cascade.detectMultiScale(eye_img,
#                                             scaleFactor=1.2,
#                                             minNeighbors=5)
#     for (x, y, w, h) in eye_rect:
#         cv2.rectangle(eye_img, (x, y),
#                       (x + w, y + h), (255, 255, 255), 10)
#     return eye_img


# Reading in the image and creating copies
img = cv2.imread('s.jpg')
img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()

# Detecting the face
face = adjusted_detect_face(img_copy1)
# print(face)
plt.imshow(face)
# Saving the image
cv2.imwrite('face10.jpg', face)
