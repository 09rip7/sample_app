import pytesseract
import cv2


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\marcu\AppData\Local\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(1)
count = 0
while True:


    ret, Frame = cap.read()

    grey = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Frame', Frame)


    if cv2.waitKey(1) & 0xFF == ord('s'):
        count = count + 1
        cv2.imwrite('image' + str(count) + '.png', Frame)
        print(count)
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

x = pytesseract.image_to_string("image" + str(count) + ".png")


cap.release()
cv2.destroyAllWindows()
print(x)
