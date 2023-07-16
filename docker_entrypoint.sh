#!/bin/sh
python3 -c "import nltk ; nltk.download(['stopwords','punkt'])"
gunicorn --chdir src --bind 0.0.0.0:9001 --workers 4 --timeout 180 wsgi:app
