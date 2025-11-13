import cv2
import PIL.Image as Image
cap = cv2.VideoCapture(0)
from chat import get_limits


##########
# Define the color to track (BGR format) for example the coor blue :
# in this case we detect blue color , and if you want to change other color (red for example ) you need to add some mofication in chat.py
our_color = [255,0,0]
##########


while True :
    ret, frame = cap.read()
    if not ret:
        print('no frame')
        break
    HsvImage = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color = our_color)

    mask = cv2.inRange(HsvImage , lowerLimit , upperLimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    print (bbox)
    if bbox:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

