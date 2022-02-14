from flask import Flask
from flask_restful import reqparse, Api, Resource
import pickle
import numpy as np
import pandas as pd
import os

# Criar objeto Flask e API para determinar métodos (GET)
app = Flask(__name__)
api = Api(app)

# Importar classificador Random Forest
path = r'C:\Users\casoto\Desktop\Fraude'
os.chdir(path)
clf_path = 'C:/Users/casoto/Desktop/Fraude.sav'
f = 'classificador.sav'
model = pickle.load(open(f, 'rb'))

# Criar objeto Parser para avaliar parâmetros enviados pelo consumidor da API (usuário)
parser = reqparse.RequestParser()
parser.add_argument('query')

# Criar classe para criar métodos (neste caso, apenas GET para prever fraudes)
class PredictFraud(Resource):
    def get(self):
        # Armazenar query enviada pelo usuário
        args = parser.parse_args()
        user_query = args['query'] # Exemplo: '215 31 19 1 0 0 0 1 1 0 0'

        # Transformar query em vetor (DF > values > reshape) e realizar predições
        uq_vectorized = user_query.split(' ')
        uq_vectorized = list(map(int, uq_vectorized))
        uq_vectorized = pd.DataFrame(uq_vectorized).values.reshape(1, -1)
        prediction = model.predict(uq_vectorized)
        pred_proba = model.predict_proba(uq_vectorized)

        # Outputs das predições em texto (normal/fraude)
        if prediction == 0:
            pred_text = 'Normal'
        else:
            pred_text = 'Fraude'

        # Arredondar probabilidade de predição das classes
        confidence = round(pred_proba[0][0], 3)

        # Output em formato JSON
        output = {'prediction': pred_text, 'confidence': confidence}
        return output

# Rotear o uso da API para o diretório raiz/atual (endpoint)
api.add_resource(PredictFraud, '/')


if __name__ == '__main__':
    """
    UTILIZAÇÃO:
        *Via Jupyter Notebook
            url = 'http://127.0.0.1:5000/'
            params ={'query': 'v1 v2 v3...'}
            response = requests.get(url, params)
            response.json()
        *OU via curl (terminal)
            curl -X GET http://127.0.0.1:5000/ -d query='v1 v2 v3...'
        *OU via HTTPie (terminal)
            http http://127.0.0.1:5000/ query=='v1 v2 v3...'
    """
    app.run(debug = True)