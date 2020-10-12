import json

from flask import Flask, request
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


def wrap_sents(sents):
    if sents == None:
        return {"sents": None}
    output = [{"id": item.id, "content": item.content} for item in sents]
    output = {"sents": output}
    return output


@app.route('/search', methods=['GET', 'POST'])
def search():
    try:
        data = request.json
        query = data["query"]
        print(query)
    except:
        query = None
    if query == None:
        sents = corpus.search()
        output = wrap_sents(sents)
        return jsonify(output)
    else:
        sents = corpus.search(query)
        output = wrap_sents(sents)
        return jsonify(output)


@app.route('/conll')
def conll():
    return app.send_static_file('conll.html')


if __name__ == "__main__":
    app.run()
