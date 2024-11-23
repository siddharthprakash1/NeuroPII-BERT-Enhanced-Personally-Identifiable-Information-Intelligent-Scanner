from flask import Flask, render_template, request, redirect, url_for
from data_scanner import scan_file
from database import store_scan_result, get_all_scans, delete_scan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        scan_result = scan_file(file)
        store_scan_result(scan_result)
        return redirect(url_for('scan_results'))
    return redirect(url_for('index'))

@app.route('/scan_results')
def scan_results():
    scans = get_all_scans()
    return render_template('scan_results.html', scans=scans)

@app.route('/delete_scan/<int:scan_id>')
def delete_scan_route(scan_id):
    delete_scan(scan_id)
    return redirect(url_for('scan_results'))

if __name__ == '__main__':
    app.run(debug=True)