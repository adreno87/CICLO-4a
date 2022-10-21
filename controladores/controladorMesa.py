from modelos.mesa import Mesa
from repositorios.repositorioMesa import RepositorioMesa


class ControladorMesa():

    def __init__(self):
        print("controlador creado")

    def getMesa(self):
        mesas = RepositorioMesa().findAll()
        return mesas

    def createMesa(self, datosMesa):
        print("se ha creado una mesa")
        _mesa = Mesa(datosMesa)
        return _mesa.__dict__

    def updateMesa(self, id, datosMesa):
        print("Actualizando mesa con id ", id)
        _mesa = Mesa(datosMesa)
        return _mesa.__dict__

    def deleteMesa(self, id):
        print("Mesa " + id + " eliminado")
        materia = {
            "id": "1",
            "numero": "5",
            "cantidad inscritos": "30"
        }
        return mesa