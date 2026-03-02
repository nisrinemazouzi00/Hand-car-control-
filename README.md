# 🚗🖐 Hand Controlled Car Game

> Control a car using your **real hand movements** with computer vision!  
> Built with **OpenCV + MediaPipe + Pygame**

---

## 🎮 Demo Preview

![Game Preview](https://via.placeholder.com/800x400?text=Hand+Controlled+Car+Game)

---

## ✨ Features

- 🖐 Real-time hand tracking using MediaPipe
- 📷 Webcam-based gesture control
- 🚗 Smooth car movement
- 🛣️ Infinite scrolling road animation
- ⚡ 30 FPS gameplay
- 🎯 No keyboard required!

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core programming language |
| OpenCV | Webcam capture & image processing |
| MediaPipe | Hand tracking & landmark detection |
| Pygame | Game development & rendering |

---

## 🧠 How It Works

1. Webcam captures your hand.
2. MediaPipe detects hand landmarks.
3. The palm base (landmark 9) is tracked.
4. X position is mapped to screen width.
5. Car smoothly follows your hand movement.

### Hand Tracking Logic

```python
x_norm = hand_landmarks.landmark[9].x
return int(x_norm * WIDTH)
```

### Smooth Movement

```python
car_x += (target_x - car_x) * 0.2
```

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/hand-controlled-car.git
cd hand-controlled-car
```

### 2️⃣ Install dependencies

```bash
pip install opencv-python mediapipe pygame
```

### 3️⃣ Add Required Images

Make sure these files exist in your project folder:

```
car.png
road.png
```

### 4️⃣ Run the Game

```bash
python main.py
```

---

## 🎯 Controls

| Action | How |
|--------|-----|
| Move Left | Move your hand left |
| Move Right | Move your hand right |
| Exit | Close the window |

---

## 🚀 Future Improvements

- Add obstacles & collision detection  
- Add scoring system  
- Add sound effects  
- Add gesture-based acceleration  
- Add start menu UI  

---

## 🧩 Project Structure

```
hand-controlled-car/
 ├── main.py
 ├── car.png
 ├── road.png
 └── README.md
```

---

## 👩‍💻 Author

**Nisrine**  
Computer Science Student  
Interested in AI • Security • Software Development 🚀

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
