# 🧠 AI Algorithms Hub

A comprehensive **Flask web application** showcasing various **AI algorithms** and **problem-solving techniques** with interactive **visualizations** and intuitive interfaces.

---

## 📁 Project Structure

```
AI-Lab-EX/
│
├── app.py                      # Main Flask application
│
├── modules/                    # Backend modules
│   ├── __init__.py
│   ├── puzzle_solver.py       # 8-Puzzle solver logic
│   ├── image_classifier.py    # Image classification logic
│   ├── nqueens_solver.py      # N-Queens CSP solver
│   └── pathfinding.py         # Pathfinding algorithms
│
├── templates/                  # HTML templates
│   ├── home.html              # Home page
│   ├── puzzle.html            # 8-Puzzle game
│   ├── classifier.html        # Image classifier
│   ├── nqueens.html           # N-Queens CSP
│   └── pathfinding.html       # Pathfinding visualizer
│
├── uploads/                    # Temporary upload folder
│
├── imagenet_classes.txt       # ImageNet class labels
│
└── requirements.txt           # Python dependencies
```

---

## 🚀 Features

### 🔹 1. 8-Puzzle Solver
- Interactive 3×3 puzzle board
- **A\*** search with Manhattan & Misplaced Tile heuristics
- Real-time **animated solution visualization**
- Move counter & shuffle functionality

### 🔹 2. Image Classifier
- Upload images for AI-based classification
- **Pre-trained GoogLeNet (Inception v1)** model
- Displays **Top-5 predictions** with confidence scores
- Supports **1000+ ImageNet categories**

### 🔹 3. N-Queens CSP
- Solve the **N-Queens problem** with customizable board size
- **Constraint Satisfaction** using backtracking
- Multiple solutions with board visualization
- Navigate between solutions easily

### 🔹 4. Pathfinding Visualizer
- Compare **8 search algorithms** (BFS, DFS, UCS, A*, etc.)
- **Tamil Nadu district map** for realistic graph visualization
- Step-by-step animation of exploration & shortest path
- Algorithm performance comparison (nodes, cost, time)

---

## 📋 Prerequisites

- Python **3.8+**
- `pip` package manager

---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rahul-Sundarraj/AI-Lab-EX.git
   cd AI-Lab-EX
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create necessary folders (if not present)**
   ```bash
   mkdir uploads
   mkdir modules
   touch modules/__init__.py       # On Windows: type nul > modules\__init__.py
   ```

---

## 📦 Requirements.txt

```
Flask==3.0.0
Flask-CORS==4.0.0
torch==2.1.0
torchvision==0.16.0
Pillow==10.1.0
```

---

## 🏃‍♂️ Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open in your browser**
   ```
   http://localhost:5000
   ```

---

## 🎯 Usage Guide

### 🏠 Home Page
- Navigate through available AI projects
- Each project card links to an interactive demo

### 🧩 8-Puzzle Solver
1. Click **“Shuffle”** to randomize tiles  
2. Move tiles manually or let AI solve it  
3. Choose a heuristic (**Manhattan / Misplaced Tile**)  
4. Watch the **animated solving process**

### 🖼️ Image Classifier
1. Upload an image (drag or select)  
2. Click **“Classify Image”**  
3. View **Top-5 AI predictions** with confidence scores  

### 👑 N-Queens CSP
1. Enter board size (N)  
2. Click **“Solve”**  
3. Browse through multiple valid solutions  

### 🗺️ Pathfinding Visualizer
1. Select a **search algorithm**  
2. Choose **start** & **goal** districts  
3. Click **“Start Search”** to visualize exploration and final path  

---

## 🧩 API Endpoints

### 8-Puzzle
- `POST /api/puzzle/shuffle` – Shuffle puzzle  
- `POST /api/puzzle/move` – Move a tile  
- `POST /api/puzzle/solve` – Solve puzzle  
- `POST /api/puzzle/reset` – Reset puzzle  

### Image Classifier
- `POST /api/classify` – Classify uploaded image  

### N-Queens
- `POST /api/nqueens/solve` – Solve N-Queens  

### Pathfinding
- `POST /api/pathfinding/search` – Run selected algorithm  
- `GET /api/pathfinding/districts` – Retrieve district data  

---

## 🔍 Algorithms Implemented

### Search Algorithms
- **BFS** – Breadth-First Search  
- **DFS** – Depth-First Search  
- **UCS** – Uniform Cost Search  
- **Depth-Limited Search**  
- **Iterative Deepening Search**  
- **Greedy Best-First Search**  
- **A\*** Search  
- **AO\*** Algorithm  

### Heuristics
- **Manhattan Distance**  
- **Misplaced Tiles**  
- **Euclidean Distance**  

### Machine Learning
- **GoogLeNet (Inception v1)** – Image Classification  

### CSP
- **Backtracking** – N-Queens Solver  

---

## 🎨 Technologies Used

| Category | Technologies |
|-----------|---------------|
| **Backend** | Flask, Python |
| **Frontend** | HTML5, CSS3, JavaScript |
| **AI/ML** | PyTorch, Torchvision |
| **Algorithms** | A\*, BFS, DFS, CSP, Heuristics |
| **Visualization** | SVG Animations, CSS Transitions |

---

## 📝 Notes

- GoogLeNet model weights are downloaded automatically on first run  
- Solving very large **N-Queens** may take longer  
- Pathfinding visualizer is best experienced on desktop browsers  
- Uploaded files are **auto-cleaned** after classification  

---

## 🤝 Contributing

Contributions are welcome!  
If you’d like to add more algorithms, optimize performance, or enhance UI:
1. Fork the repository  
2. Create a new branch (`feature/your-feature`)  
3. Commit and push your changes  
4. Submit a Pull Request 🎉  

---

## 📄 License

This project is open-source and available for **educational and research purposes**.

---

## 👨‍💻 Author

Rahul-Sundarraj [GitHub](https://github.com/Rahul-Sundarraj/AI-Lab-EX.git)

**Developed with ❤️ using Flask & Modern Web Technologies.**  
> _“Bringing AI concepts to life through visualization.”_
