from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('layouts/index.html',
                           title="FreeTrak", flash_message="True")


@app.route('/upload', methods=['POST'])
def upload():
    print(request.files)
    return "True"


if __name__ == '__main__':
    app.run(host='localhost')
