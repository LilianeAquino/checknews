import unittest
import json
from server import app


class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def testReturn200(self):
        data = {
            'text': 'OMS disse que vacinas contra Covid-19 não são necessárias para crianças e adolescentes saudáveis',
            'origin': 'https://twitter.com/fatooufake/status/1644419772392566817?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet'
            }
        response = self.app.post('/api/classifier', json=data)
        self.assertEqual(response.status_code, 200)


    def testReturn200WithoutOrigin(self):
        data = {
            'text': 'OMS disse que vacinas contra Covid-19 não são necessárias para crianças e adolescentes saudáveis',
            'origin': ''
            }
        response = self.app.post('/api/classifier', json=data)
        self.assertEqual(response.status_code, 200)


    def testReturn400WithoutText(self):
        data = {
            'text': '',
            'origin': 'https://twitter.com/fatooufake/status/1644419772392566817?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet'
            }
        response = self.app.post('/api/classifier', json=data)
        self.assertEqual(response.status_code, 400)


    def testReturnClassification(self):
        data = {
            'text': 'OMS disse que vacinas contra Covid-19 não são necessárias para crianças e adolescentes saudáveis',
            'origin': 'https://twitter.com/fatooufake/status/1644419772392566817?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet'
            }
        response = self.app.post('/api/classifier', json=data)
        self.assertEqual(json.loads(response.data.decode('utf-8')), {"classification":{"confianca": 0.9395386735686593, "label": "Notícia falsa"}})


if __name__ == '__main__':
    unittest.main()
