import cv2

class BlackAndWhiteFilter:
    def apply(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)  # Convert back to 3-channel BGR
