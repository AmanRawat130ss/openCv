import cv2 as cv

def rescaleframe(frame, scale = 0.5):

    ''' only work for image , videos and live video '''

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width*1,height)

    return cv.resize(frame, dimensions,  interpolation= cv.INTER_AREA)

img = cv.imread('Memes/s.jpg')
# cv.imshow('cartooon', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('grey', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rec = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1 , minNeighbors = 1)

print(f'number face = {len(face_rec)}')

for(x,y,w,h) in face_rec:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=5)



resize_image = rescaleframe(img)
cv.putText(resize_image,"M", (20,150), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,0,255), 2)
cv.imshow("Resized image",resize_image)

# cv.imshow("Dectacted Faces", img)
cv.waitKey(0)

