from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('resume.json', 'r') as f:
        data = json.load(f)
    return render_template('index.html', resume=data)

@app.route('/api')
def api():
    with open('resume.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
