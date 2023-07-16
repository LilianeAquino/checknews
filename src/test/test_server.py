import json
import unittest
from unittest.mock import patch
from server import app


class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()


    @patch('modules.ml.classifier.predictAll')
    def testReturnClassification(self, mock_predictAll):
        mock_predictAll.return_value = {
            "classification": {
                "confianca": 0.9395386735686593,
                "label": "Notícia falsa"
            }
        }

        data = {
            'text': 'OMS disse que vacinas contra Covid-19 não são necessárias para crianças e adolescentes saudáveis',
            'origin': 'https://twitter.com/fatooufake/status/1644419772392566817?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet'
        }

        response = self.app.post('/api/classifier', json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.data.decode('utf-8')),
            {"classification": {"confianca": 0.9395386735686593, "label": "Notícia falsa"}}
        )


    @patch('modules.ml.classifier.predictAll')
    def testReturn200(self, mock_predictAll):
        mock_predictAll.return_value = {"classification": {"confianca": 0.9, "label": "fake"}}

        data = {
            'text': 'OMS disse que vacinas contra Covid-19 não são necessárias para crianças e adolescentes saudáveis',
            'origin': 'https://twitter.com/fatooufake/status/1644419772392566817?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet'
        }

        response = self.app.post('/api/classifier', json=data)
        self.assertEqual(response.status_code, 200)


    @patch('modules.ml.classifier.predictAll')
    def testReturn200WithoutOrigin(self, mock_predictAll):
        mock_predictAll.return_value = {"classification": {"confianca": 0.9, "label": "fake"}}

        data = {
            'text': 'OMS disse que vacinas contra Covid-19 não são necessárias para crianças e adolescentes saudáveis',
            'origin': ''
        }

        response = self.app.post('/api/classifier', json=data)
        self.assertEqual(response.status_code, 200)


    @patch('modules.ml.classifier.predictAll')
    def testReturn400WithoutText(self, mock_predictAll):
        mock_predictAll.return_value = {"classification": {"confianca": 0.9, "label": "fake"}}

        data = {
            'text': '',
            'origin': 'https://twitter.com/fatooufake/status/1644419772392566817?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet'
        }

        response = self.app.post('/api/classifier', json=data)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
