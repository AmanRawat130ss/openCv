import cv2 as cv

# img = cv.imread('Memes/peter.jpg')

# cv.imshow('SpiderMan',img)

cap = cv.VideoCapture('video/b.mp4')
while True:
    isTrue,frame = cap.read()
   
    cv.imshow('video',frame)

    if cv.waitKey(5) & 0xFF==ord('d'):
        break
cap.release()
cv.destroyAllWindows
cv.waitKey(0)
