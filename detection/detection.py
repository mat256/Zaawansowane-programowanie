import numpy as np
import cv2
import imutils
from imutils.object_detection import non_max_suppression
import time


def detection(file: str):
    start = time.time()
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    frame = cv2.imread(file)
    size = frame.shape[:2]
    frame = imutils.resize(frame, width=min(800, frame.shape[1]))

    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    boxes, weights = hog.detectMultiScale(frame, winStride=(3, 3),
                                          padding=(8, 8))

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    boxes = non_max_suppression(boxes, probs=None, overlapThresh=0.63)

    # print(len(boxes))
    for (xA, yA, xB, yB) in boxes:
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                      (0, 255, 0), 2)
    end = time.time()
    cv2.putText(frame, "Detected: " + str(len(boxes)) + " in: " + str(round(end - start, 2)) + "s", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                cv2.FONT_HERSHEY_SIMPLEX)
    cv2.putText(frame, str(size), (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                cv2.FONT_HERSHEY_SIMPLEX)
    cv2.imshow('frame', frame)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return len(boxes)
