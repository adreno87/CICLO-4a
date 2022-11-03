from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controladores.controladorCandidato import CandidatoControlador
from controladores.controladorPartido import PartidoControlador
from controladores.controladorMesa import MesaControlador

app = Flask(__name__) 
cors = CORS(app)

"""RUTAS DE ADMIN --> CANDIDATO"""

"""LISTAR CANDIDATOS (GET)"""
@app.route("/candidato",methods=['GET'])
def getCandidatos():
    json=CandidatoControlador.get()
    return jsonify(json)

"""CREAR UN CANDIDATO - (POST)"""
@app.route("/candidato",methods=['POST'])
def createCandidato():
    dataEntrada = request.get_json()
    dataSalida=CandidatoControlador.create(dataEntrada)
    return jsonify(dataSalida)

"""ELIMINAAR UN CANDIDATO - (DELETE)"""
@app.route("/candidato/<string:id>",methods=['DELETE'])
def deleteCandidato(id):
    json=CandidatoControlador.delete(id)
    return jsonify(json)

"""ACTUALIZAR UN CANDIDATO - (PUT)"""
@app.route("/candidatos/<string:id>", methods=['PUT'])
def actualizarCandidato(id):
    data = request.get_json()
    json = CandidatoControlador.update(id, data)
    return jsonify(json)

"""BUSCAR CANDIDADTO - (GET)"""
@app.route("/candidatos/<string:id>", methods=['GET'])
def buscarCandidato(id):
    json = CandidatoControlador.find(id)
    return jsonify(json)

"""ASIGNAR PARTIDO A UN CANDIDATO - (PUT)"""
@app.route("/candidato/<string:id>/partido/<string:id_partido>", methods=['PUT'])
def asignarPartido(id, id_partido):
    json = CandidatoControlador.asignarPartido(id, id_partido)
    return jsonify(json)


"""LISTAR PARTIDOS (GET)"""
@app.route("/partido",methods=['GET'])
def getPartidos():
    json=PartidoControlador.getPartido()
    return jsonify(json)

"""CREAR UN PARTIDO - (POST)"""
@app.route("/partido",methods=['POST'])
def createPartido():
    dataEntrada = request.get_json()
    dataSalida=PartidoControlador.createPartido(dataEntrada)
    return jsonify(dataSalida)

"""ELIMINAAR UN PARTIDO - (DELETE)"""
@app.route("/partido/<string:id>",methods=['DELETE'])
def deletePartido(id):
    json=PartidoControlador.deletePartido(id)
    return jsonify(json)

"""ACTUALIZAR UN PARTIDO - (PUT)"""
@app.route("/partido/<string:id>", methods=['PUT'])
def actualizarPartido(id):
    data = request.get_json()
    json = PartidoControlador.updatePartido(id, data)
    return jsonify(json)

#PATH MESA

"""LISTAR MESAS (GET)"""
@app.route("/mesa",methods=['GET'])
def getMesa():
    json=MesaControlador.get()
    return jsonify(json)

"""CREAR UN MESA - (POST)"""
@app.route("/mesa",methods=['POST'])
def createMesa():
    dataEntrada = request.get_json()
    dataSalida=MesaControlador.create(dataEntrada)
    return jsonify(dataSalida)

"""ACTUALIZAR UN MESA - (PUT)"""
@app.route("/mesa/<string:id>", methods=['PUT'])
def actualizarMesa(id):
    data = request.get_json()
    json = MesaControlador.update(id, data)
    return jsonify(json)

"""BUSCAR MESA - (GET)"""
@app.route("/mesa/<string:id>", methods=['GET'])
def buscarMesa(id):
    json = MesaControlador.find(id)
    return jsonify(json)

"""ELIMINAAR UN MESA - (DELETE)"""
@app.route("/mesa/<string:id>",methods=['DELETE'])
def deleteMesa(id):
    json=MesaControlador.delete(id)
    return jsonify(json)






###############################################
"""CARGAR UN ARCHIVO DE CONFIGURACIÓN"""
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data







    

"""INICIANDO LA APLICACIÓN"""
if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))

    #Configurar un servidor de aplicaciones
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])