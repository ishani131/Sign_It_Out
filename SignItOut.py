import cv2
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW) # accessing webcam
limit = 10  # set the limit
cascade = [cv2.CascadeClassifier("cascade\{0}.xml".format(i)) for i in range(5)]
# creating 26 cascade classifier objects
limit_var = 0
while True:
    ref = 0
    temp = 0

    success, img = vid.read()
    for i in range(5):
          x = list(cascade[i].detectMultiScale(img,1.1,5))
        ref = ord(i + 65)
    if(len(x)!=0):
        t = temp
        temp = ref
    if(t == temp):
        limit_var+=1
    if(limit_var > limit):
        print(ref)
        limit_var = 0
    cv2.imshow("hi", img)  # this is the video output window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()







