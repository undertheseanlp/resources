from flask import Flask

app = Flask(__name__, static_url_path='/', static_folder='app')


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/amr')
def amr():
    return app.send_static_file('amr.html')


@app.route('/conll')
def conll():
    return app.send_static_file('conll.html')


if __name__ == "__main__":
    app.run()
