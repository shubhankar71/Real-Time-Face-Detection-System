# 🎯 Real-Time Face Detector using OpenCV

A Python-based real-time face detection program that uses your webcam and OpenCV's Haar Cascade Classifier to detect and highlight faces live.

---

## 📸 Demo

> Detects faces in real-time through your webcam, draws green rectangles around each face, and shows the live face count on screen.

https://drive.google.com/file/d/12hlqELCR1evcT-lOqBnu04WUhc1G-Uzo/view?usp=sharing

---

## 🚀 Features

- Real-time face detection using webcam
- Green bounding box drawn around each detected face
- Live face count displayed on screen
- Lightweight — runs entirely on CPU using Haar Cascades
- Simple one-file script, easy to understand and modify

---

## 🛠️ Requirements

- Python 3.7+
- OpenCV

Install dependencies:

```bash
pip install opencv-python
```

---

## ▶️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/shubhankar71/Real-Time-Face-Detection-System
cd Real-Time-Face-Detection-System
```

2. **Install dependencies**

```bash
pip install opencv-python
```

3. **Run the script**

```bash
python face_detector.py
```

4. **Press `Q`** to quit the program.

---

## 📁 Project Structure

```
📦 your-repo-name
 ┣ 📄 face-detector.py   # Main face detection script
 ┣ 📄 requirements.txt   # Python dependencies
 ┗ 📄 README.md          # Project documentation
```

---

## ⚙️ How It Works

1. Opens your default webcam using `cv2.VideoCapture(0)`
2. Each frame is converted to **grayscale** (Haar Cascade works on grayscale images)
3. The `detectMultiScale` function scans the frame for faces using a pre-trained Haar Cascade model
4. Detected faces are highlighted with a **green rectangle** and a `"Face"` label
5. Total face count is displayed in the top-left corner of the window

---

## 🔧 Configuration

You can tweak these parameters in `face_detector.py` to adjust detection sensitivity:

| Parameter | Default | Description |
|---|---|---|
| `scaleFactor` | `1.1` | How much the image is reduced at each scale |
| `minNeighbors` | `5` | Higher = fewer false detections |
| `minSize` | `(30, 30)` | Minimum face size to detect (in pixels) |

---

## 📦 requirements.txt

```
opencv-python
```

---
## ⚠️ Limitations

While this project is efficient for real-time applications, it has some known constraints:

* **ighly optimized for frontal faces; struggles with side profiles or tilted angles.
* **Accuracy drops in low-light environments or under harsh shadows.
* **Recognition can fail if features are partially covered by masks, hands, or sunglasses.
* **Complex background textures may occasionally be misidentified as faces.
* **Being a Haar Cascade-based system, it is faster on low-end CPUs but less robust than modern Deep Learning models (like MediaPipe or SSD).
