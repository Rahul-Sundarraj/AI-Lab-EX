from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

# Import modules
from modules import puzzle_solver, image_classifier, nqueens_solver, pathfinding

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# ============== HOME PAGE ==============
@app.route('/')
def index():
    return render_template('home.html')

# ============== 8-PUZZLE GAME ==============
@app.route('/puzzle')
def puzzle():
    return render_template('puzzle.html')

@app.route('/api/puzzle/shuffle', methods=['POST'])
def puzzle_shuffle():
    data = request.json
    steps = data.get('steps', 30)
    state = puzzle_solver.random_shuffle(steps)
    return jsonify({
        'state': list(state),
        'solvable': puzzle_solver.is_solvable(state)
    })

@app.route('/api/puzzle/move', methods=['POST'])
def puzzle_move():
    data = request.json
    state = tuple(data['state'])
    tile = data.get('tile')
    result = puzzle_solver.move_tile(state, tile)
    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result)

@app.route('/api/puzzle/solve', methods=['POST'])
def puzzle_solve():
    data = request.json
    state = tuple(data['state'])
    heuristic = data.get('heuristic', 'manhattan')
    result = puzzle_solver.solve_puzzle(state, heuristic)
    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result)

@app.route('/api/puzzle/reset', methods=['POST'])
def puzzle_reset():
    return jsonify({'state': list(puzzle_solver.GOAL)})

# ============== IMAGE CLASSIFICATION ==============
@app.route('/classifier')
def classifier():
    return render_template('classifier.html')

@app.route('/api/classify', methods=['POST'])
def classify_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not image_classifier.allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400
    
    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        results, error = image_classifier.classify_image(filepath)
        
        if error:
            return jsonify({'error': f'Classification failed: {error}'}), 500
        
        os.remove(filepath)
        
        return jsonify({'predictions': results})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============== N-QUEENS CSP ==============
@app.route('/nqueens')
def nqueens():
    return render_template('nqueens.html')

@app.route('/api/nqueens/solve', methods=['POST'])
def nqueens_solve():
    data = request.get_json() or {}
    result = nqueens_solver.solve_nqueens(data)
    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result)

# ============== PATHFINDING ALGORITHMS ==============
@app.route('/pathfinding')
def pathfinding_page():
    return render_template('pathfinding.html')

@app.route('/api/pathfinding/search', methods=['POST'])
def pathfinding_search():
    data = request.json
    result = pathfinding.execute_search(data)
    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result)

@app.route('/api/pathfinding/districts')
def get_districts():
    return jsonify(pathfinding.TN_DISTRICTS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)