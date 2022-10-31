from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controladores.controladorCandidato import ControladorCandidato
from controladores.controladorPartido import PartidoControlador
from controladores.controladorMesa import ControladorMesa

app = Flask(__name__) #instancia de la clase Flask
cors = CORS(app)

"""RUTAS DE API (PATH)"""

#PATH CANDIDATOS -listar
_controlador_candidato = ControladorCandidato()
ControladorPartido = PartidoControlador()

@app.route("/candidatos", methods=["GET"])
def get_candidatos():
    datos = _controlador_candidato.getCandidato()
    return jsonify(datos)

#PATH CANDIDATOS -Eliminar
@app.route("/candidatos/<string:id>", methods=["DELETE"])
def delete_candidato(id):
    datos = _controlador_candidato.deleteCandidato(id)
    return jsonify(datos)

#PATH CANDIDATOS -Crear
@app.route("/candidatos", methods=["POST"])
def create_candidato():
    datosEntrada = request.get_json()
    datosSalida = _controlador_candidato.createCandidato(datosEntrada)
    return jsonify(datosSalida)

#PATH CANDIDATOS -Actualizar
@app.route("/candidatos/<string:id>", methods=["PUT"])
def modificarCandidato(id):
    data = request.get_json()
    json = ControladorCandidato.updateCandidato(id,data)
    return jsonify(json)


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

    #PATH MESA -Actualizar
@app.route("/mesas/<string:id>", methods=["PUT"])
def modificarMesa(id):
    data = request.get_json()
    json = ControladorMesa.updateMesa(id,data)
    return jsonify(json)


"""LISTAR MESA (GET)"""
@app.route("/mesa",methods=['GET'])
def getPartidos():
    json=ControladorMesa.getMesa()
    return jsonify(json)

"""CREAR UNA MESA - (POST)"""
@app.route("/mesa",methods=['POST'])
def createMesa():
    dataEntrada = request.get_json()
    dataSalida=ControladorMesa.createMesa(dataEntrada)
    return jsonify(dataSalida)

"""ELIMINAAR UNA MESA - (DELETE)"""
@app.route("/mesa/<string:id>",methods=['DELETE'])
def deleteMesa(id):
    json=ControladorMesa.deleteMesa(id)
    return jsonify(json)

"""ACTUALIZAR UNA MESA - (PUT)"""
@app.route("/mesa/<string:id>", methods=['PUT'])
def actualizarMesa(id):
    data = request.get_json()
    json = ControladorMesa.updateMesa(id, data)
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