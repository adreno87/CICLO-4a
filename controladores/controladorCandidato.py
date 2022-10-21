from modelos.candidato import Candidato
from repositorios.repositorioCandidato import RepositorioCandidato


class ControladorCandidato():

    def __init__(self):
        print("controlador creado")

    def getCandidato(self):
        candidatos = RepositorioCandidato().findAll()
        print(candidatos)
        return candidatos

    def createCandidato(self, datosCandidato):
        print("se ha creado un candidato")
        _candidato = Candidato(datosCandidato)
        return _candidato.__dict__

    def updateCandidato(self, id, datosCandidato):
        print("Actualizando candidato con id ", id)
        elCandidato = Candidato(datosCandidato)
        return elCandidato.__dict__

    def deleteCandidato(self, id):
        print("Candidato " + id + " eliminado")
        candidato = {
            "id": "1",
            "nombre": "juan",
            "apellido": "Garces"
        }
        return candidato