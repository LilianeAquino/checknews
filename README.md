<h1 align="center">Checknews: Plataforma web para detecção de fake news</h1>

[![Python Version][python-image]][python-url]
[![Sklearn Version][scikit-learn-image]][scikit-learn-url]

## Configuração de desenvolvimento
<p align="justify">Gere um ambiente virtual e baixe as dependências do projeto: </p>

~~~Python
pip3.8 install -r requirements.txt 
~~~

_Em caso de dúvidas, consulte este [artigo sobre ambiente virtual][ambiente-url]._

<p align="justify">Para executar o projeto: </p>

~~~Python
python3.8 src/server.py
~~~

## Padrão de estilo PEP8

<p>Para verificar se o código está seguindo o padrão de estilo PEP8, rode o seguinte comando:<p>

~~~Python
 flake8 caminho/nome_arquivo
~~~

_Consulte a [documentação das regras do Flake8][flake8-url]._ 

<p>Para verificar se o código tem algum problema com a tipagem dos dados, rode o seguinte comando:<p>

~~~Python
 mypy caminho/nome_arquivo
~~~

_Consulte a [documentação do MyPy][mypy-url]._

<p>Para executar os testes, execute o projeto localmente e, em outro terminal, rode o seguinte comando:<p>

~~~Python
 python3.8 -m unittest discover ./src/ "test_*.py"
~~~

[ambiente-url]: https://tutorial.djangogirls.org/pt/django_installation/
[python-url]: https://www.python.org/downloads/release/python-3810/
[python-image]: https://img.shields.io/badge/python-v3.8.10-blue
[flake8-url]: https://www.flake8rules.com/
[mypy-url]: https://mypy.readthedocs.io/en/stable/
[scikit-learn-image]: https://img.shields.io/badge/scikit--learn-v1.2.1-brightgreen
[scikit-learn-url]: https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html
