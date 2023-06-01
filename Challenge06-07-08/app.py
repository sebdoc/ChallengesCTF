from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/index.html')
def index2():
    return send_from_directory('templates', 'index.html')

@app.route('/images/bon.png')
def image1():
    return send_from_directory('images', 'bon.png')

@app.route('/images/boff.png')
def image2():
    return send_from_directory('images', 'boff.png')

@app.route('/flag2.html')
def flag2():
    return send_from_directory('templates', 'flag2.html')

@app.route('/flag3.html')
def flag3():
    return send_from_directory('templates', 'flag3.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181)
