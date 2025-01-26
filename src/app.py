import os
import subprocess
import html
from flask import Flask, request, jsonify

app = Flask(__name__)
UPLOAD_FOLDER = './src/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
OUTPUT_FILE = os.path.join(UPLOAD_FOLDER, 'output.json')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def index():
    return '''
    <!doctype html>
    <title>Upload JSON</title>
    <h1>Upload a JSON file</h1>
    <form method=post enctype=multipart/form-data action="/upload">
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.json'):
        file_path = os.path.join(UPLOAD_FOLDER, 'file.json')
        file.save(file_path)
        
        # Execute the TemplateAnalyzer command
        command = f'/usr/local/bin/TemplateAnalyzer/TemplateAnalyzer analyze-template {file_path} --report-format Sarif -o {OUTPUT_FILE}'
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            with open(OUTPUT_FILE, 'r') as f:
                output_content = f.read()
            encoded_output = html.escape(output_content)
            return f'''
            <!doctype html>
            <title>Analysis Result</title>
            <h1>Analysis Result</h1>
            <pre>{encoded_output}</pre>
            <a href="/">Upload another file</a>
            '''
        except Exception as e:
            encoded_error = html.escape(str(e))
            return jsonify({'error': encoded_error}), 500

    return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)