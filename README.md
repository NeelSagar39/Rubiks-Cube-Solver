# 🤊 Rubik's Cube Solver

This project hosts a simple Express.js web server that allows you to **take a picture of a Rubik's Cube from your phone**, detect the cube’s colors, generate a matrix representation, and calculate the **most optimal moves to solve it**.

Whether you're speedcubing or just stuck on a colorful mess, this tool helps you solve it quickly and efficiently.

---

## 📸 How It Works

1. Open the website hosted by the server on your **mobile phone**.
2. **Take a picture** of each side of your Rubik's Cube.
3. The app processes the images to build a **3x3x6 color matrix**.
4. An optimal solution (series of moves) is calculated and displayed.
5. You solve your cube, guided by the step-by-step solution.

---

## 🛠️ Folder Structure

```bash
project-root/
├── public/
│   ├── cube_images/          # Stores captured cube face images
│   ├── cube_solver/          # Solver logic and utilities
│   ├── images/               # Additional assets (icons, UI)
│   ├── ImageUploader.js      # Handles image upload logic
│   ├── index.html            # Web interface
│   ├── result.png            # Output image with solution (example)
│   └── tables.json           # Color recognition or cube data
├── .gitignore
├── package.json
├── package-lock.json
├── result.png                # Possibly generated result image
└── README.md
```

---

## ✨ Getting Started

### Prerequisites

* Node.js (v14+ recommended)
* npm

### Install Dependencies

```bash
npm install
```

### Run the Server

```bash
node server.js
```

(If your entry file is named differently, e.g. `app.js`, adjust accordingly.)

### Access the App

* Open your browser or phone and go to:
  `http://localhost:3000`
  (or your LAN IP if accessing from another device)

---

## 📦 Features

* Mobile-friendly UI
* Capture and upload cube face images
* Detect cube colors
* Generate optimal solving steps
* Display moves visually

---

## 📷 Sample Output

![Result](./result.png)

---

## 🧠 Credits

This project was created with love and the intent of **revolutionising the world** — one Rubik's Cube at a time.

---

## 📝 License

MIT License – feel free to use, remix, or improve!

