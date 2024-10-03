import cv2

class MirrorFilter:
    def apply(self, frame):
        return cv2.flip(frame, 1)  # Flip horizontally
