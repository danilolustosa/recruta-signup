from flask import Flask, request
from flask_cors import CORS, cross_origin
#pip install -U flask-cors

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/candidato/inserir', methods=['POST'])
def inserirCandidato():  
    print(request.data)    
    return { 'message': 'Candidato salvo com sucesso' }
    
