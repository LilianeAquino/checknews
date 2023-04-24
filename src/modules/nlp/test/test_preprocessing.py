import sys
sys.path.append('/home/liliane_aquino/Estudos/TCC - PUC/checknews_backend/src')

import unittest
import warnings
from modules.nlp.pre_processing import pre_processor


warnings.filterwarnings('ignore')


class TestPreProcessor(unittest.TestCase):
    def testCleaning(self):
        text = 'OMS disse que vacinas contra Covid-19 não são necessárias para crianças e adolescentes saudáveis'
        expected = 'oms disse vacinas contra covid decimalTag nao necessarias criancas adolescentes saudaveis'
        self.assertEqual(pre_processor.cleaning(text), expected)


    def testPrepareData(self):
        text = 'https://twitter.com/fatooufake/status/1644419772392566817?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet'
        expected = 'https://twitter.com/fatooufake/status/1644419772392566817?ref src=twsrc%5egoogle%7ctwcamp%5eserp%7ctwgr%5etweet'
        self.assertEqual(pre_processor.prepareData(text), expected)


    def testReplaceTag(self):
        text = 'Olá, meu email é email@example.com e meu telefone é (11) 9999-9999'
        expected = 'Olá, meu email é  emailTag  e meu telefone é  telefoneTag '
        self.assertEqual(pre_processor.replaceTag(text), expected)


    def testRemoveHtml(self):
        text = '<p>Exemplo de <b>texto</b> com <i>tags</i> <a href="https://www.google.com">HTML</a></p>'
        expected = 'Exemplo de texto com tags HTML'
        self.assertEqual(pre_processor.removeHtml(text), expected)


    def testRemoveStopwords(self):
        text = 'Este é um exemplo de texto com palavras irrelevantes'
        expected = 'Este exemplo texto palavras irrelevantes'
        self.assertEqual(pre_processor.removeStopwords(text), expected)


    def testRemoveEmojis(self):
        text = 'Olá! 😃👍 Como você está se sentindo hoje? 😔'
        expected = 'Olá!   Como você está se sentindo hoje?  '
        self.assertEqual(pre_processor.removeEmojis(text), expected)


    def testNormalizeText(self):
        text = 'Olá, como está você hoje?'
        expected = 'Ola, como esta voce hoje?'
        self.assertEqual(pre_processor.normalizeText(text), expected)


    def testRemovePunctuation(self):
        text = 'Tudo bem?!! #aprendizado?'
        expected = 'Tudo bem     aprendizado '
        self.assertEqual(pre_processor.removePunctuation(text), expected)


    def testReplaceBlanks(self):
        text = 'Tudo bem\n\naprendizado '
        expected = 'Tudo bem  aprendizado '
        self.assertEqual(pre_processor.replaceBlanks(text), expected)


    def testClearText(self):
        text = 'Tudo bem  aprendizado '
        expected = 'Tudo bem aprendizado'
        self.assertEqual(pre_processor.clearText(text), expected)


if __name__ == '__main__':
    unittest.main()     
