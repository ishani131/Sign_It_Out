import cv2
import time
str1 = ""
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW) # accessing webcam
limit = 10  # set the limit
cascade = [cv2.CascadeClassifier("cascade\{0}.xml".format(i)) for i in range(26)]
# creating 26 cascade classifier objects
limit_var = 0
while True:
    ref = ""
    temp = ""
    success, img = vid.read()
    for i in range(26):
        x = list(cascade[i].detectMultiScale(img,1.1,5))
        ref = ord(i + 65)
    if(len(x)!=0):
        t = temp
        temp = ref
    if(t == temp):
        limit_var+=1
    if(limit_var > limit):
        str1 += str(ref)
        limit_var = 0
    cv2.imshow("OutputWindow", img)  # this is the video output window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(3)
print(str1)
vid.release()
cv2.destroyAllWindows()