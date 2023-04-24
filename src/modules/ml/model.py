import numpy as np
from cloudpickle import load
from sklearn.pipeline import Pipeline


PATH = 'src/model/'

class Model():
    def load_model(self) -> Pipeline:
        with open(PATH+'classifier_model.sav', 'rb') as model:
            classifier_model = load(model)
        return classifier_model


    def predict(self, text: str, origin: str) -> dict:
        model = self.load_model()

        probabilities = model[0].predict_proba([[text, origin]])[0]
        index = np.argmax(probabilities)
        label = model[1].inverse_transform([index])[0]
        maxProbability = probabilities[index]
        return {'label': label, 'maxProbability': maxProbability}
