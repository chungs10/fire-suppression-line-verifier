import numpy as np
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.image_name_edit = QLineEdit()
        self.save_button = QPushButton("Save Image")
        self.reset_largest_button = QPushButton('Reset')
        self.reset_largest_button.clicked.connect(self.resetContours)
        self.quit_button = QPushButton('Finish and Exit')
        self.quit_button.clicked.connect(self.terminateApplication)
        self.image_label = QLabel()
        self.largestContour = None
        self.largestLength = 0
        self.running = True

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter Image Name:"))
        layout.addWidget(self.image_name_edit)
        layout.addWidget(self.save_button)
        layout.addWidget(self.image_label)
        layout.addWidget(self.reset_largest_button)
        layout.addWidget(self.quit_button)

        self.save_button.clicked.connect(self.save_image)

        self.setLayout(layout)
        self.setWindowTitle("Image Processing")
        
        self.destroyed.connect(self.terminateApplication)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint)

    def terminateApplication(self):
        self.running = False
    
    def resetContours(self):
        self.largestContour = None
        self.largestLength = 0
    
    def save_image(self):
        image_name = self.image_name_edit.text()
        if not image_name:
            return
        image_path = f"./static/database/template/{image_name}_{self.largestLength}.jpg"
        cv2.imwrite(image_path, self.current_image)
        print(f"Image saved as {image_path}")

    def show_image(self, image):
        height, width, _ = image.shape
        bytes_per_line = 3 * width
        q_img = QPixmap.fromImage(QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888))
        self.image_label.setPixmap(q_img)

    def process_image(self, image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        h, w = img.shape[:2]
        blurred = cv2.GaussianBlur(img, (3, 3), 0)
        edged = cv2.Canny(blurred, 10, 100)
        
        alpha = 0.5  # Adjust transparency (0: fully transparent, 1: fully opaque)

        # Find contours directly on the grayscale image
        contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Filter contours to only keep horizontal lines
        horizontal_contours = []
        for cnt in contours:
            x, y, wC, hC = cv2.boundingRect(cnt)
            if hC / wC < 0.05:  # Adjust this threshold based on the expected aspect ratio of horizontal lines
                horizontal_contours.append(cnt)

        # Draw all horizontal contours with different colors
        vis = np.zeros((h, w, 3), np.uint8)
        for cnt in horizontal_contours:
            color = tuple(map(int, np.random.randint(0, 255, size=3)))
            cv2.drawContours(vis, [cnt], -1, color, 2)
        
        # Draw the contour with maximum perimeter (omitting the first contour which is outer boundary of image
        # Not necessary in this case
        vis2 = np.zeros((h, w, 3), np.uint8)
        perimeter=[]
        for cnt in horizontal_contours[1:]:
            perimeter.append(cv2.arcLength(cnt,True))
            x, y, wC, hC = cv2.boundingRect(cnt)
            if wC > self.largestLength:
                self.largestLength = wC
                maxindex= perimeter.index(max(perimeter))
                self.largestContour = [horizontal_contours[maxindex+1]]                
                
        if not self.largestContour == None:
            cv2.drawContours( vis, self.largestContour, 0, (0,255,0), 50)
            cv2.drawContours( vis2, self.largestContour, 0, (0,255,0), 50)
        
        if len(perimeter) == 0:
            blended_img = cv2.addWeighted(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR), 1-alpha, vis, alpha, 0)
            return blended_img

        # Overlay 'vis' on top of 'img'
        blended_img = cv2.addWeighted(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR), 1-alpha, vis2, alpha, 0)

        return blended_img

    def process_and_show_image(self, image):
        processed_image = self.process_image(image)
        self.show_image(processed_image)
        self.current_image = processed_image

def main():
    # Initialize the Qt application
    app = QApplication([])

    # Create the main window
    window = MainWindow()
    window.resize(800, 600)
    window.show()

    # Open the video capture device
    cap = cv2.VideoCapture(1)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while window and window.running:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Process and show the frame in the UI
        try:
            window.process_and_show_image(frame)
        except:
            pass

        # Process events to keep the UI responsive
        app.processEvents()

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

    # Terminate the application
    app.quit()

if __name__ == "__main__":
    pass
