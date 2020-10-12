from os.path import join, dirname

from flask import Flask
from flask import jsonify
from data import CONLLCorpus, CONLLFactory
from corpus import corpus
app = Flask(__name__, static_url_path='/', static_folder='.')



@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/amr')
def amr():
    return app.send_static_file('amr.html')


@app.route('/search')
def search():
    print(CONLLCorpus)
    output = corpus.search()
    output = [{"id": item.id, "content": item.content} for item in output]
    output = {"sents": output}
    return jsonify(output)


@app.route('/conll')
def conll():
    return app.send_static_file('conll.html')


if __name__ == "__main__":
    app.run()
