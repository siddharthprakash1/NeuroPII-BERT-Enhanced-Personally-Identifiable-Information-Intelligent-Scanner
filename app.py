from flask import Flask, render_template, request, redirect, url_for
from data_scanner import SensitiveDataScanner, scan_file
from database import store_scan_result, get_all_scans, delete_scan

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    
    if file and (file.filename.endswith('.csv') or 
                 file.filename.endswith('.xlsx') or 
                 file.filename.endswith('.xls') or
                 file.filename.endswith('.doc') or
                 file.filename.endswith('.docx')):
        scan_result = scan_file(file)
        store_scan_result(scan_result)
        return redirect(url_for('scan_results'))
    
    return 'Invalid file type'

@app.route('/scan_results')
def scan_results():
    scans = get_all_scans()
    return render_template('scan_results.html', scans=scans)

@app.route('/delete_scan/<int:scan_id>')
def delete_scan_route(scan_id):
    delete_scan(scan_id)
    if not get_all_scans():  # If no scans remaining
        return redirect(url_for('index'))  # Redirect to upload page
    return redirect(url_for('scan_results'))
if __name__ == '__main__':
    app.run(debug=True)