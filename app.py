from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_recognition', methods=['POST'])
def run_recognition():
    try:
        result = subprocess.run(['python', 'FaceRecognition.py'], capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({"message": "Face recognition completed successfully!"})
        else:
            return jsonify({"message": "Error running face recognition script!", "error": result.stderr})
    except Exception as e:
        return jsonify({"message": "An unexpected error occurred!", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)



