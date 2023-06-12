import os
import platform
import sklearn
from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv
from flask import Flask, jsonify, request, abort

from modules.ml.classifier import predictAll, getLogs


load_dotenv(verbose=True)


client = MongoClient(getenv('URL_MONGO'))
dbname = client[getenv('DB_NAME')]
collection = dbname[getenv('COLLECTION')]


app = Flask(__name__)


@app.route('/api/health', methods=['GET'])
def getVersion():
    return jsonify({
      'version': '1.0',
      'projeto': 'Checknews: Plataforma web para detecção de fake news',
      'python': platform.python_version(),
      'sklearn': sklearn.__version__
    })


@app.route('/api/classifier', methods=['POST'])
def classify():
    if request.json is not None and request.json != {}:
        if request.json.get('text') and request.json['text'] != '':
            text = str(request.json['text']).strip()
            origin = str(request.json['origin']).strip()
        else:
            collection.insert_one(getLogs({'text': None, 'origin': None, 'classification': {}, 'success': False, 'error': 'Invalid request - problems with parameters passed via post'}))
            abort(400)
    else:
        collection.insert_one(getLogs({'text': None, 'origin': None, 'classification': {}, 'success': False, 'error': 'Invalid request - problems with parameters passed via post'}))
        abort(400)

    result = predictAll(text, origin)
    return jsonify({'classification': result})


if __name__ == '__main__':
    port = int(os.getenv('PORT_CLASSIFIER', default=8002))
    app.run(host='0.0.0.0', port=port, debug=True)
