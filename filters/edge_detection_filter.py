import cv2

class EdgeDetectionFilter:
    def apply(self, frame):
        return cv2.Canny(frame, 100, 200)
