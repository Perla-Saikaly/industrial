from flask import Flask, render_template, redirect
import subprocess
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/train')
def train():
    subprocess.Popen(['python', 'train.py'])
    return redirect('/')

@app.route('/gui')
def gui():
    subprocess.Popen(['python', r'GUI\handwritten.py'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)