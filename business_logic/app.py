from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/train')
def train():
    # TODO: Add logic for train route
    return redirect("http://127.0.0.1:8001/train")

@app.route('/gui')
def gui():
    # TODO: Add logic for gui route
    return redirect("http://127.0.0.1:8003/gui")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)