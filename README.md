
# Face Recognition System

![Face Recognition System Logo](https://github.com/Levi-Chinecherem/face-recognition-system/blob/main/sample%20output/Screenshot%20(6).png)

The Face Recognition System is an application that uses the face_recognition library to recognize and label faces in a real-time video stream. This README provides detailed information about the system, its features, requirements, installation, and usage.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Real-Time Face Recognition: The system can recognize and label faces in real-time using a computer's webcam.
- Training from Images: Train the system by providing a set of known faces along with their labels.
- High Accuracy: The system uses the face_recognition library, which is known for its high accuracy in face recognition.
- Customization: You can easily customize the system to add more features, such as name tagging, logging, and more.

## Requirements

- Python 3.x
- face_recognition
- OpenCV (cv2)
- Webcam or camera (for real-time recognition)
- Training images of known faces (for training)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Levi-Chinecherem/face-recognition-system.git
   ```
2. Create a virtual environment (recommended) and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
4. Organize your training images:

   - Create a folder named "training."
   - Inside the "training" folder, create subfolders for each person you want to recognize.
   - Place images of each person in their respective subfolders.
5. Train the system:

   - Run the training script to encode and save known face encodings:

   ```bash
   python train.py
   ```
6. Start the face recognition system:

   ```bash
   python recognize_faces.py
   ```

## Usage

1. The system will use your computer's webcam to capture frames in real-time.
2. It will recognize and label faces if they match the known faces from your training data.
3. Recognized faces will be labeled with their respective names on the screen.

![Face Recognition System Screenshot](https://github.com/Levi-Chinecherem/face-recognition-system/blob/main/sample%20output/Screenshot%20(11).png)

## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

Please ensure your code follows best practices and includes test cases if applicable.

## License

This project is licensed under the [MIT License](LICENSE).

© 2023 Levi Chinecherem C.
