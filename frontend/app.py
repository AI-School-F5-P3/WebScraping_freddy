import sys
import os
from flask import Flask, render_template, request, jsonify
import logging
import pandas as pd

# Añade el directorio 'src' al path de Python para poder importar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import Database

app = Flask(__name__)

# Configuración de logging
logging.basicConfig(filename='logs/frontend.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

@app.route('/')
def index():
    try:
        logging.info("Iniciando el proceso de recuperación de datos")
        db = Database()
        quotes = db.get_all_quotes()
        db.close()
        logging.info(f"Se recuperaron {len(quotes)} frases")
        return render_template('index.html', quotes=quotes.to_dict('records'))
    except Exception as e:
        logging.error(f"Error al recuperar datos: {str(e)}")
        return "Error al cargar los datos", 500

@app.route('/search')
def search():
    tags = request.args.get('query', '').split(',')
    author = request.args.get('author', '')
    db = Database()
    
    quotes = db.get_all_quotes()
    
    if tags and tags[0]:
        quotes = quotes[quotes['tags'].apply(lambda x: any(tag.strip().lower() in x.lower() for tag in tags))]
    
    if author:
        quotes = quotes[quotes['author'].str.lower() == author.lower()]
    
    db.close()
    return render_template('quotes.html', quotes=quotes.to_dict('records'))

@app.route('/get_filters')
def get_filters():
    db = Database()
    all_quotes = db.get_all_quotes()
    tags = set(tag.strip() for tags in all_quotes['tags'].str.split(',') for tag in tags)
    authors = set(all_quotes['author'])
    db.close()
    return jsonify({'tags': sorted(list(tags)), 'authors': sorted(list(authors))})

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)