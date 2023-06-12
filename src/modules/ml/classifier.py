from modules.nlp.pre_processing.pre_processor import cleaning, prepareData
from modules.ml.assets.labels import labels
from modules.ml.model import Model
from datetime import datetime
from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv


load_dotenv(verbose=True)


client = MongoClient(getenv('URL_MONGO'))
dbname = client[getenv('DB_NAME')]
collection = dbname[getenv('COLLECTION')]


model = Model()


def predictAll(text: str, origin: str) -> tuple:
    """
        Método responsável por executar o pipeline de classificação
    """
    cleanedText = cleaning(text)
    cleanedOrigin = prepareData(origin)
    classification = model.predict(cleanedText, cleanedOrigin)

    try:
        collection.insert_one(getLogs({'text': text, 'origin': origin, 'classification': classification, 'success': True, 'error': None}))
    except Exception as error:
        collection.insert_one(getLogs({'text': text, 'origin': origin, 'classification': classification, 'success': False, 'error': str(error)}))

    return {
        'label': labels[classification['label']],
        'confianca': classification['maxProbability']
    }


def getLogs(params: dict) -> dict:
    """
        Método responsável por gerar os logs da aplicação
    """
    current_datetime = datetime.now()
    log = {
            'date': current_datetime,
            'text': params.get('text'),
            'origin': params.get('origin'),
            'classification': params.get('classification'),
            'success': params.get('success'),
            'error': params.get('error')
        }
    return log
