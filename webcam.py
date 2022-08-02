import cv2

camera = cv2.VideoCapture(0)

while True:
    _, frame = camera.read()
    cv2.imshow("frame",frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
