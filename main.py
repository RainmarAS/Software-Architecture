import cv2
from filters.black_white_filter import BlackAndWhiteFilter
from filters.mirror_filter import MirrorFilter
from filters.resize_filter import ResizeFilter
from filters.edge_detection_filter import EdgeDetectionFilter

class VideoFilterPipeline:
    def __init__(self, video_source=0):
        """Initializes the video capture and filter pipeline."""
        self.cap = cv2.VideoCapture(video_source)  # Use 0 for webcam, or path for video
        self.filters = []

    def add_filter(self, video_filter):
        """Adds a filter to the pipeline."""
        self.filters.append(video_filter)

    def process(self):
        """Processes the video frame-by-frame, applying the filters."""
        if not self.cap.isOpened():
            print("Error: Unable to open video source.")
            return

        while True:
            ret, frame = self.cap.read()  # Capture frame-by-frame
            if not ret:
                print("Error: Failed to grab frame.")
                break

            # Apply all filters in sequence
            for video_filter in self.filters:
                frame = video_filter.apply(frame)

            # Show the processed frame
            cv2.imshow('Video Filter Pipeline', frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()  # Release the capture
        cv2.destroyAllWindows()  # Close all OpenCV windows

if __name__ == '__main__':
    # Initialize the video filter pipeline (0 for webcam, or path to video file)
    pipeline = VideoFilterPipeline("C:\\Users\\aboin\Downloads\\file_example_MP4_480_1_5MG.mp4")

    # Add filters to the pipeline
    pipeline.add_filter(BlackAndWhiteFilter())  # Black and white filter
    pipeline.add_filter(MirrorFilter())         # Mirror effect filter
    pipeline.add_filter(ResizeFilter(0.7))      # Resize to 70%
    pipeline.add_filter(EdgeDetectionFilter())  # Edge detection filter

    # Process video stream and apply filters
    pipeline.process()
