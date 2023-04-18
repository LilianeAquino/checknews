import os
import platform
import sklearn
from flask import Flask, jsonify, request, abort

from modules.ml.classifier import predictAll


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
    if request.json is not None:
        text = str(request.json['text']).strip()
        origin = str(request.json['origin']).strip()
    else:
        abort(400)

    result = predictAll(text, origin)
    return jsonify({'classification': result})


if __name__ == '__main__':
    port = int(os.getenv('PORT_CLASSIFIER', default=8002))
    app.run(host='0.0.0.0', port=port, debug=True)
