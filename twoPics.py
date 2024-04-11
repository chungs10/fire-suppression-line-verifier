import numpy as np
import cv2
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QImage, QPixmap

running = True

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize UI components
        self.select_image_button = QPushButton('Select Template Image')
        self.select_image_button.clicked.connect(lambda: self.setTemplateBool(self.select_image()))
        self.reset_largest_button = QPushButton('Reset')
        self.reset_largest_button.clicked.connect(self.resetContours)
        # self.quit_button = QPushButton('Finish and Exit')
        # self.quit_button.clicked.connect(self.terminateApplication)
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.live_feed_label = QLabel()
        self.live_feed_label.setAlignment(Qt.AlignCenter)
        self.largestContour = None
        self.largestLength = 0
        self.templateLength = 0

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.select_image_button)
        innerLayout = QHBoxLayout()
        innerLayout.addWidget(self.image_label)
        innerLayout.addWidget(self.live_feed_label)
        layout.addLayout(innerLayout)
        layout.addWidget(self.reset_largest_button)
        # layout.addWidget(self.quit_button)
        self.setLayout(layout)
        
        self.destroyed.connect(self.terminateApplication)
        # self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint)

        # Open the video capture device (default webcam)
        self.cap = cv2.VideoCapture(1)

        # Check if the webcam is opened successfully
        if not self.cap.isOpened():
            print("Error: Could not open webcam.")
            sys.exit(1)

    def terminateApplication(self):
        # Quit the application
        # self.cap.release()
        # cv2.destroyAllWindows()
        running = False
        print("Closing application")
    
    def resetContours(self):
        self.largestContour = None
        self.largestLength = 0
    
    def setTemplateBool(self, res):
        if res:
            # If a template image is selected, start capturing live feed
            self.resetContours()
            self.start_live_feed()
    
    def start_live_feed(self):
        # Loop to continuously read frames from the webcam
        while running:
            # Capture frame-by-frame
            ret, frame = self.cap.read()

            # Check if the frame was read successfully
            if not ret:
                print("Error: Could not read frame.")
                break

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            h, w = img.shape[:2]
            blurred = cv2.GaussianBlur(img, (3, 3), 0)
            edged = cv2.Canny(blurred, 10, 100)

            # Find contours directly on the grayscale image
            contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Filter contours to only keep horizontal lines
            horizontal_contours = []
            for cnt in contours:
                x, y, wC, hC = cv2.boundingRect(cnt)
                if hC / wC < 0.1:  # Adjust this threshold based on the expected aspect ratio of horizontal lines
                    horizontal_contours.append(cnt)

            # Draw all horizontal contours with different colors
            vis = np.zeros((h, w, 3), np.uint8)
            for cnt in contours:
                if cv2.contourArea(cnt) > 500:
                    color = tuple(map(int, np.random.randint(0, 255, size=3)))
                    cv2.drawContours(vis, [cnt], -1, color, 3)
            
            # draw the largest horizontal contour thicket
            perimeter=[]
            if len(horizontal_contours) > 0:
                #cv2.drawContours(vis, [horizontal_contours[0]], -1, (0,255,0), 50)
                for cnt in horizontal_contours[1:]:
                    perimeter.append(cv2.arcLength(cnt,True))
                    x, y, wC, hC = cv2.boundingRect(cnt)
                    if wC > self.largestLength:
                        self.largestLength = wC
                        maxindex= perimeter.index(max(perimeter))
                        self.largestContour = [horizontal_contours[maxindex+1]]
            
            if not self.largestContour == None:
                cv2.drawContours( vis, self.largestContour, 0, (0,255,0), 50)

            # Overlay 'vis' on top of 'img'
            alpha = 0.5  # Adjust transparency (0: fully transparent, 1: fully opaque)
            blended_img = cv2.addWeighted(frame, 1-alpha, vis, alpha, 0)

            if float(self.largestLength) > 0 and ((abs(float(self.largestLength) - float(self.templateLength)) / float(self.templateLength) < .1) or (float(self.largestLength) >= float(self.templateLength))):
                cv2.rectangle(blended_img, (0, 0), (w-1, h-1), (0,255,0), 30)
            else:
                cv2.rectangle(blended_img, (0, 0), (w-1, h-1), (255,0,0), 30)

            # Display the blended image
            # Convert the frame to QImage
            h, w, c = blended_img.shape
            q_img = QImage(blended_img.data, w, h, c * w, QImage.Format_RGB888)

            # Display live feed
            self.live_feed_label.setPixmap(QPixmap.fromImage(q_img))

            # Process events to keep the UI responsive
            QApplication.processEvents()

        # Release the capture
        self.cap.release()
        cv2.destroyAllWindows()

    def select_image(self):
        # Open file dialog to select an image
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open Image', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        
        # Check if an image is selected
        if file_path:
            try:
                self.templateLength = file_path.split('_')[-1].split('.')[0]
            except:
                pass
            
            # Read the selected image
            image = cv2.imread(file_path)
            
            # Convert the image to RGB format
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Convert the image to QImage
            h, w, c = image_rgb.shape
            q_img = QImage(image_rgb.data, w, h, c * w, QImage.Format_RGB888)

            # Display the selected image
            self.image_label.setPixmap(QPixmap.fromImage(q_img))
            return True
        return False

def main():
    # Initialize the Qt application
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()
    window.setWindowTitle('Live Feed and Image Display')
    window.resize(800, 600)
    window.show()
    
    app.aboutToQuit.connect(window.terminateApplication)
    sys.exit(app.exec_())

if __name__ == "__main__":
    pass
