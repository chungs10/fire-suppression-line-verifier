# Project Overview: United Airlines Cargo Hold Compliance Verifier
A full-stack web application prototype developed in collaboration with **United Airlines** to automate the safety inspection process for aircraft cargo holds. The system uses computer vision to verify that luggage and cargo are stored below the fire suppression line.

- United Airlines: A major American airline headquartered in Chicago
- Established in 1926, with a broad network of global flights
- Key hubs: Chicago, Denver, Houston, Newark
- Point person - Mr. Anthony Haloulos (Engagement Analyst, United Airlines)
- Known for commitment to high-quality customer service

# Problem Statement
The United Airlines ramp employees do not have a standardized checklist for ensuring proper distribution of luggage weight, and luggage strapping which could result in imbalances during flight and non-compliance when luggage surpasses the fire suppression line.

# Goals
- Elevating employee and customer experience through efficient loading
processes.
- Utilizing technology for improved safety and compliance.

## Tech Stack

*Backend:* Python, Flask, OpenCV  
*Frontend:* HTML, CSS, JavaScript, Bootstrap  
*Database:* MongoDB  
*Computer Vision:* Custom image processing algorithms for dimension mapping and compliance checking  
*Methodology:* Agile Development, Client Feedback Loops

## Key Features

- Image Upload and Capture interface for ramp agents
- Digital mapping of cargo hold dimensions and fire suppression line
- Computer Vision algorithm to analyze luggage placement
- Compliance Pass/Fail verification with visual feedback
- Secure storage of images and audit logs in MongoDB

# Python pip installs
- pip install opencv-python numpy keras tensorflow pyqt5 Pillow flask flask_cors

# How to run:
- From the main United folder, run `python router.py`
- Once the initial processes are complete, navigate to 127.0.0.1:5000 in a browser

# Other notes:
- The machine learning model is not included since the file is large. Contact the group to get the trained model
- For future improvement: the twoPics.py program may not terminate properly, future todo is reconfigure the QApplication to terminate completely when the subprogram is exited. This issue comes up when the "Live Analysis" button is clicked
