import pytesseract
from PIL import Image
import cv2

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\marcu\AppData\Local\Tesseract-OCR\tesseract.exe'

#f = Image.open('images.png')

#print(f)

#x = pytesseract.image_to_string(f)
#jasmine = pytesseract.image_to_data(f)

#print(x)
#print(jasmine)

#img = cv2.imread('funnyy.jpg', 0)

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)   //creates an empty window


# cv2.imwrite('funnygray.jpg', img)
# cv2.imshow('funny', img)
#
# print(img)
# cv2.waitKey(1)
# cv2.destroyAllWindows()
# cv2.imshow('pizza', img)
# k = cv2.waitKey(0)
# if k == ord('s'):
#     cv2.imwrite('newsav.png', img)
#     cv2.destroyAllWindows()
# elif k == 27:0
#     cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

#define codexx and videowriter objects  /* makes it so you can apply the one setting to all parameters

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    #capture frame by frame
    ret, frame = cap.read()
    #operations on frame(changing it to grey)
    #
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #color = cv2.cvtColor(frame, cv2.COLOR_BGR)

    #display the resulting frames
    xcv = cv2.imshow('Frame', gray)
    # we use 1 in waitkey so that it keeps the video feed contiuously runing instead of capturing a single frame
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        pass
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#when everything is done release the capture
cap.release()
cv2.destroyAllWindows()

# while cap.isOpened():
#     ret, frame = cap.read()
#
#     if ret == True:
#         frame = cv2.flip(frame, 1)
#         out.write(frame)
#
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# cap.release()
# out.release()
# cv2.destroyAllWindows()





