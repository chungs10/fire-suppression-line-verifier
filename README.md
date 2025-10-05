# United Airlines Cargo Hold Compliance Verifier


A functional proof-of-concept developed for United Airlines to explore the viability of automating safety inspections using computer vision. This capstone project demonstrates a full-stack system that analyzes aircraft cargo hold images to verify luggage is stored below the fire suppression line.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=OpenCV&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

## Features

* **Computer Vision Analysis:** Implements custom algorithms using OpenCV to digitally map cargo hold dimensions and identify the fire suppression line.
* **Compliance Verification:** Analyzes uploaded images to detect if luggage placement breaches the suppression line, providing an immediate Pass/Fail result with visual feedback.
* **Web Interface:** Provides United Airlines ramp agents with an intuitive, browser-based tool for image capture and upload.
* **Data Integrity & Audit Logging:** Securely stores all inspection images and results in a MongoDB database for compliance tracking and accountability.
* **Client-Centric Development:** Built using an Agile methodology with continuous feedback from United Airlines stakeholders.


## Tech Stack

* **Frontend:** HTML, CSS, JavaScript, Bootstrap
* **Backend:** Python, Flask, OpenCV
* **Database:** MongoDB
* **Computer Vision:** Custom image processing algorithms for dimension mapping and compliance checking
* **Methodology:** Agile Development, Client Feedback Loops


## System Architecture


A layered architecture supporting the computer vision pipeline:
- **Frontend:** HTML/CSS/JavaScript interface for United Airlines ramp agents
- **Backend API:** Flask server with REST endpoints for image processing
- **Vision Engine:** Custom OpenCV algorithms for suppression line detection
- **Persistence:** MongoDB document store for inspection records and audit trails


## Installation & Usage

### Prerequisites
* Python 3.8+
* MongoDB installed and running
   
### Installation
* Clone the repository and install dependencies:
```bash
git clone https://github.com/chungs10/fire-suppression-line-verifier.git
cd fire-suppression-line-verifier
pip install -r requirements.txt
```

### Run the application:
1. Start the server
```bash
python router.py
```
2. Access the web interface:
    Navigate to http://127.0.0.1:5000 in your browser.

### Usage
-  Upload cargo hold images through the web interface
-  View compliance results with visual annotations
-  Access audit logs in the MongoDB database


## Project Structure
```plaintext
fire-suppression-line-verifier/
├── app/
│   ├── router.py             # Main Flask application entry point
│   ├── imageProcessing.py    # Core computer vision algorithms
│   ├── captureTemplate.py    # Template image capture utilities
│   ├── twoPics.py            # Live image analysis module
│   └── united_model.json     # Trained computer vision model weights
├── static/
│   ├── css/                  # Stylesheets for web interface
│   ├── images/               # Application assets & United Airlines branding
│   ├── js/                   # Frontend JavaScript for user interactions
│   ├── video/                # Demonstration and tutorial videos
│   └── uploads/              # User image storage and processing results
├── templates/                # HTML templates for web interface
├── tests/
│   └── test.py               # Testing utilities and validation
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```


## Team & Contributions

This project was developed as part of the **IT Capstone** curriculum at Rensselaer Polytechnic Institute. It was a collaborative effort by a team of four students.

My contributions included:
* **Frontend Development:** Built HTML templates and client-side interface components using JavaScript, CSS, and Bootstrap
* **Frontend-Backend Integration:** Established data flow patterns and integration points that served as the foundation for Flask backend implementation  
* **Client Collaboration:** Implemented UI/UX improvements based on feedback from United Airlines stakeholders

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Notes
* **Model Weights Availability:** The trained computer vision model weights file is not included due to size constraints. Contact Raphael Chung for academic inquiries.
* **Known Software Issue:** The twoPics.py subprocess may not terminate correctly after using the "Live Analysis" feature, leaving a dormant QApplication instance. The exit handler requires reconfiguration to ensure a clean exit.


## Acknowledgements

We thank Mr. Anthony Haloulos of the United Airlines Innovation Lab for sponsoring this project and for his guidance as our client sponsor. 
