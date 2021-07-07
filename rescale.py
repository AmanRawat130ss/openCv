import cv2 as cv



def rescaleframe(frame, scale = 0.2):

    ''' only work for image , videos and live video '''

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions,  interpolation= cv.INTER_AREA)


img = cv.imread('Memes/me.jpg')
cv.imshow('Bugs',img)

resize_image = rescaleframe(img)
cv.imshow("resixed image",resize_image)

# cap = cv.VideoCapture('video/b.mp4')
# while True:
#     isTrue,frame = cap.read()
#     frame_resize = rescaleframe(frame)
   
#     cv.imshow('video',frame)
#     cv.imshow('Video Resize', frame_resize)

#     if cv.waitKey(5) & 0xFF==ord('d'):
#         break

    
# cap.release()
cv.destroyAllWindows
cv.waitKey(0)