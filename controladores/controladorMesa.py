from modelos.mesa import Mesa
from repositorios.RepositorioMesa import RepositorioMesa

class MesaControlador():
    
    def __init__(self):
        print("Creando ControladorMesa")  
        self.mesa_repo = RepositorioMesa()  
        
    def getMesa(self):
        mesas = self.mesa_repo.findAll()
        return mesas
    
    def createMesa(self, datosMesa):
        mesa = Mesa(datosMesa)
        datos_salida = self.mesa_repo.save(mesa)
        return datos_salida
    
    def updateMesa(self, id, datosMesa):
        buscar_mesa = self.mesa_repo.findById(id)
        mesa = Mesa(buscar_mesa)
        mesa.numero = datosMesa["numero"]
        mesa.numero_inscritos = datosMesa["numero_inscritos"]
        self.mesa_repo.save(mesa)
        return mesa.__dict__ 
        
    def deleteMesa(self, id):
        print("Mesa " + id + " eliminada")
        mesa = self.mesa_repo.delete(id)
        return mesa       