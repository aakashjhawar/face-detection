# Face Detection

A fast and accurate face detection with OpenCV using a pre-trained deep learning face detector model shipped with the library.
Two files are required for using OpenCV's deep neural network module with Caffe models.
- The .prototxt file (define the model architecture i.e., the layers themselves)
 - The .caffemodel file (which contains the weights for the actual layers)

## Getting Started

How to use
```    
git clone https://github.com/aakashjhawar/face-detection.git
cd face-detection
python3 detect_faces_image.py <path/to/input_image>
```
## Prerequisites

- Python 3.5
- OpenCV
```
sudo apt-get install python-opencv
```

## Results

#### Face detection from group photo-
![Result](https://github.com/aakashjhawar/face-detection/blob/master/images/result1.png)