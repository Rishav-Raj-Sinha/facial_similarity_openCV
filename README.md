# Face Recognition System

This project implements a simple face recognition system using Python, OpenCV, and the face_recognition library. The system can compare two faces and determine if they belong to the same person, along with calculating the similarity distance between them.

## Features

- Face detection in images
- Face encoding and comparison
- Visual representation of detected faces
- Distance measurement between face encodings
- Real-time results display on images

## Prerequisites

Before running this project, make sure you have the following dependencies installed:

```bash
pip install face_recognition
pip install opencv-python
pip install numpy
```

## Project Structure

The project requires the following structure:

```
project_root/
│
├── images/
│   ├── train.jpg        # Training image (known face)
│   └── test.jpg         # Test image to compare
│
└── face_recognition.py  # Main script
```

## Usage

1. Place your training image (known face) in the `images` directory as `train.jpg`
2. Place the test image in the `images` directory
3. Run the script:
   ```bash
   python face_recognition.py
   ```

## How It Works

The script follows these steps:

1. **Image Loading and Preprocessing**
   - Loads both training and test images
   - Converts images from BGR to RGB color format

2. **Face Detection and Encoding**
   - Detects face locations in both images
   - Generates face encodings for comparison
   - Draws rectangles around detected faces

3. **Face Comparison**
   - Compares face encodings to determine if they match
   - Calculates the distance between face encodings
   - Displays results on the test image

4. **Result Visualization**
   - Shows both images in separate windows
   - Displays match result and confidence score on the test image
   - Prints results to console

## Code Explanation

```python
# Step 1: Load and preprocess images
img_david = face_recognition.load_image_file('./images/train.jpg')
img_david = cv2.cvtColor(img_david, cv2.COLOR_BGR2RGB)

# Step 2: Detect faces and generate encodings
face_loc = face_recognition.face_locations(img_david)[0]
encode_david = face_recognition.face_encodings(img_david)[0]

# Step 3: Compare faces and calculate distance
results = face_recognition.compare_faces([encode_david], encode_test)
face_distance = face_recognition.face_distance([encode_david], encode_test)
```

## Output

The script displays:
- Two windows showing the original images with detected faces
- Visual indicators showing the face detection rectangles
- Text overlay showing the match result and confidence score
- Console output with match status and distance value

## Understanding Results

- The face distance metric ranges from 0 to 1
- Lower distance values indicate more similar faces
- Typically, a distance < 0.6 suggests a match
- The boolean result (True/False) indicates if the faces match based on a threshold

## Dependencies

- face_recognition (0.3.0 or higher)
- OpenCV (cv2) (4.0.0 or higher)
- NumPy (1.19.0 or higher)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
