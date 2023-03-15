import cv2


def mouse_callback(event, x, y, flags, param):
    global roi_selected, roi_start, roi_end, roi_window
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_selected = False
        roi_start = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        roi_end = (x, y)
        roi_selected = True

        cv2.rectangle(frame, roi_start, roi_end, (0, 255, 0), 2)

        roi_window = frame[roi_start[1]:roi_end[1], roi_start[0]:roi_end[0]]
        cv2.imshow("ROI", roi_window)


cap = cv2.VideoCapture(0)

cv2.namedWindow("Video")

cv2.setMouseCallback("Video", mouse_callback)

roi_selected = False
roi_start = (0, 0)
roi_end = (0, 0)
roi_window = None

while True:

    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
