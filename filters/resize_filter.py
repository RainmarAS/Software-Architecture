import cv2

class ResizeFilter:
    def __init__(self, scale=0.5):
        self.scale = scale

    def apply(self, frame):
        height, width = frame.shape[:2]
        new_dimensions = (int(width * self.scale), int(height * self.scale))
        if new_dimensions[0] <= 0 or new_dimensions[1] <= 0:
            print("Error: Invalid resize dimensions.")
            return frame  # Return original frame if resize is invalid
        return cv2.resize(frame, new_dimensions)
