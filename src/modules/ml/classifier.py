from modules.nlp.pre_processing.pre_processor import cleaning, prepareData
from modules.ml.model import Model


model = Model()


def predictAll(text: str, origin: str) -> tuple:
    """
        Método responsável por executar o pipeline de classificação
    """
    cleanedText = cleaning(text)
    cleanedOrigin = prepareData(origin)
    classification = model.predict(cleanedText, cleanedOrigin)

    return {
        'label': classification['label'],
        'confianca': classification['maxProbability']
    }
