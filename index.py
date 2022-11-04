from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controladores.controladorCandidato import CandidatoControlador
from controladores.controladorPartido import PartidoControlador
from controladores.controladorMesa import MesaControlador
from controladores.controladorResultados import ResultadosControlador

app = Flask(__name__) 
cors = CORS(app)

ControladorCandidato = CandidatoControlador()
ControladorPartido = PartidoControlador()
ControladorMesa = MesaControlador()
ControladorResultados = ResultadosControlador()

#RUTAS DE ADMIN --> CANDIDATO

"""LISTAR CANDIDATOS (GET)"""
@app.route("/candidato",methods=['GET'])
def getCandidatos():
    json=ControladorCandidato.getCandidato()
    return jsonify(json)

"""CREAR UN CANDIDATO - (POST)"""
@app.route("/candidato",methods=['POST'])
def createCandidato():
    dataEntrada = request.get_json()
    dataSalida=ControladorCandidato.createCandidato(dataEntrada)
    return jsonify(dataSalida)

"""ELIMINAAR UN CANDIDATO - (DELETE)"""
@app.route("/candidato/<string:id>",methods=['DELETE'])
def deleteCandidato(id):
    json=ControladorCandidato.deleteCandidato(id)
    return jsonify(json)

"""ACTUALIZAR UN CANDIDATO - (PUT)"""
@app.route("/candidato/<string:id>", methods=['PUT'])
def actualizarCandidato(id):
    data = request.get_json()
    json = ControladorCandidato.updateCandidato(id, data)
    return jsonify(json)

"""ASIGNAR PARTIDO A UN CANDIDATO - (PUT)"""
@app.route("/candidato/<string:id>/partido/<string:id_partido>", methods=['PUT'])
def asignarPartido(id, id_partido):
    json = ControladorCandidato.asignarPartido(id, id_partido)
    return jsonify(json)

#RUTAS DE ADMIN --> PARTIDO

"""LISTAR PARTIDOS (GET)"""
@app.route("/partido",methods=['GET'])
def getPartidos():
    json=ControladorPartido.getPartido()
    return jsonify(json)

"""CREAR UN PARTIDO - (POST)"""
@app.route("/partido",methods=['POST'])
def createPartido():
    dataEntrada = request.get_json()
    dataSalida=ControladorPartido.createPartido(dataEntrada)
    return jsonify(dataSalida)

"""ELIMINAAR UN PARTIDO - (DELETE)"""
@app.route("/partido/<string:id>",methods=['DELETE'])
def deletePartido(id):
    json=ControladorPartido.deletePartido(id)
    return jsonify(json)

"""ACTUALIZAR UN PARTIDO - (PUT)"""
@app.route("/partido/<string:id>", methods=['PUT'])
def actualizarPartido(id):
    data = request.get_json()
    json = ControladorPartido.updatePartido(id, data)
    return jsonify(json)

#RUTAS DE ADMIN --> MESA

"""LISTAR MESAS (GET)"""
@app.route("/mesa",methods=['GET'])
def getMesa():
    json=ControladorMesa.get()
    return jsonify(json)

"""CREAR UN MESA - (POST)"""
@app.route("/mesa",methods=['POST'])
def createMesa():
    dataEntrada = request.get_json()
    dataSalida=ControladorMesa.create(dataEntrada)
    return jsonify(dataSalida)

"""ACTUALIZAR UN MESA - (PUT)"""
@app.route("/mesa/<string:id>", methods=['PUT'])
def actualizarMesa(id):
    data = request.get_json()
    json = ControladorMesa.update(id, data)
    return jsonify(json)

"""ELIMINAAR UN MESA - (DELETE)"""
@app.route("/mesa/<string:id>",methods=['DELETE'])
def deleteMesa(id):
    json=ControladorMesa.delete(id)
    return jsonify(json)

#RUTAS DE ADMIN --> RESULTADOS

"""LISTAR RESULTADOS (GET)"""
@app.route("/resultados", methods=["GET"])
def get_resultados():
    datos = ControladorResultados.getResultados()
    return jsonify(datos)

"""CREAR UN RESULTADO - (POST)"""
@app.route("/resultados", methods=["POST"])
def create_resultados():
    datos_entrada = request.get_json()
    datos_salida = ControladorResultados.createResultados(datos_entrada)
    return jsonify(datos_salida)

"""ACTUALIZAR UN RESULTADO - (PUT)"""
@app.route("/resultados/<string:id>", methods=["PUT"])
def actualizarResultados(id):
    data = request.get_json()
    json = ControladorResultados.updateResultados(id,data)
    return jsonify(json)

"""ELIMINAR UN RESULTADO - (DELETE)"""
@app.route("/resultados/<string:id>", methods=["DELETE"])
def deleteResultado(id):
    datos = controladorResultados.deleteResultados(id)
    return jsonify(datos)



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