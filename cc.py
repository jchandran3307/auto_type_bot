from flask import Flask, render_template, request, jsonify
import subprocess
import json

app = Flask(__name__, template_folder='.')


@app.route('/')
def index():
    return render_template('hi.html')

@app.route('/run', methods=['POST'])
def run_code():
    try:
        # Read text sent from frontend
        data = request.get_json()
        text = data.get("text", "")

        # Pass the text to script.py
        result = subprocess.run(
            ["python", "script.py", text],
            capture_output=True,
            text=True
        )

        return jsonify({"message": result.stdout or result.stderr})
    except Exception as e:
        return jsonify({"message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

