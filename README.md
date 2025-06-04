# Real time object detection system with YOLOv8


This repository provides a Python-based, GPU-accelerated real-time object detection pipeline using Ultralytics’ YOLOv8 and OpenCV.  
It captures webcam input, detects objects in each frame, draws bounding boxes with confidence scores, and displays the real-time annotated video feed.

**Steps to follow:**

1. Clone this repo and go to the project:
```
git clone https://github.com/lakhmanisahil/object_detection.git
cd object_detection
```

2. Install dependencies:
```
pip install --upgrade pip
pip install -r requirements.txt
```
Note: If you plan to use GPU acceleration on Ubuntu 22.04 (CUDA 11.7 or newer), first install the appropriate torch/torchvision binaries:

``pip install torch torchvision --index-url https://download.pytorch.org/whl/cu117``

Then run:
``pip install ultralytics opencv-python numpy<2.0``

3. Running this script:
- Ensure your webcam is plugged in and recognized (check ls /dev/video* on Linux or Device Manager on Windows).
- Run: ``python main.py``

4. A window titled “Real-Time Detection” will open.
Bounding boxes with [class_name] [confidence] will appear on each detected object.
Press q to quit cleanly.
