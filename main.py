from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import datetime
import requests
import re

app=Flask(__name__)
cors = CORS(app)
from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app.config["JWT_SECRET_KEY"]="superr-secretoo"
jwt = JWTManager(app)
@app.route("/login", methods=["POST"])
def create_token():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-seguridad"]+'/usuarios/validar'
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        user = response.json()
        expires = datetime.timedelta(seconds=60 * 60*24)
        access_token = create_access_token(identity=user, expires_delta=expires)
        return jsonify({"token": access_token, "user_id": user["_id"]})
    else:
        return jsonify({"msg": "usuario o contraseña incorrecto"}), 401




@app.before_request
def before_request_callback():
    endPoint = limpiarURL(request.path)
    excludedRoutes = ["/login"]
    if excludedRoutes.__contains__(request.path):
        print("ruta excluida ", request.path)
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        if usuario["rol"] is not None:
            tienePersmiso = validarPermiso(
                endPoint, request.method, usuario["rol"]["_id"])

            if not tienePersmiso:
                return jsonify({"message": "Permission denied"}), 401
        else:
            return jsonify({"message": "Permission denied"}), 401


def limpiarURL(url):
    partes = request.path.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url = url.replace(laParte, "?")
    return url


def validarPermiso(endPoint, metodo, idRol):
    url = dataConfig["url-backend-seguridad"] + \
        "/permisos-roles/validar-permiso/rol /"+str(idRol)

    tienePermiso = False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.get(url, json=body, headers=headers)
    try:
        data = response.json()
        if ("_id" in data):
            tienePermiso = True
    except:
        pass
    return tienePermiso


@app.route("/mesas",methods=['GET'])
def get_mesas():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultados"] + '/mesas'
    response = requests.get(url, headers=headers)
    json = response.json()
    print(url)
    return jsonify(json)
@app.route("/mesas",methods=['POST'])
def create_mesas():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultados"] + '/mesas'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def getMesas(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultados"] + '/mesas/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def update_mesas(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultados"] + '/mesas/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['DELETE'])
def delete_mesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultados"] + '/mesas/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/partidos",methods=['GET'])
def get_partidos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultados"] + '/partidos'
    response = requests.get(url, headers=headers)
    json = response.json()
    print(url)
    return jsonify(json)
@app.route("/partidos",methods=['POST'])
def create_partidos():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultados"] + '/partidos'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartidos(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultados"] + '/partidos/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def update_partidos(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultados"] + '/partidos/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def delete_partidos(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultados"] + '/partidos/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)












































@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running..."
    return jsonify(json)
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data
if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":"+str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
