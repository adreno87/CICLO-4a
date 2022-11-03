from modelos.mesa import Mesa
from repositorios.RepositorioMesa import RepositorioMesa

class MesaControlador():
    
    def __init__(self):
        print("Creando ControladorMesa")  
        self.mesa_repo = RepositorioMesa()  
        
    def get(self):
        mesas = self.mesa_repo.findAll()
        return mesas
    
    def create(self, datosMesa):
        mesa = Mesa(datosMesa)
        datos_salida = self.mesa_repo.save(mesa)
        return datos_salida
    
    def update(self, id, datosMesa):
        buscar_mesa = self.mesa_repo.findById(id)
        mesa = Mesa(buscar_mesa)
        mesa.numero_mesa = datosMesa["numero_mesa"]
        mesa.cedulas_inscritas = datosMesa["cedulas_inscritas"]
        self.mesa_repo.save(mesa)
        return mesa.__dict__ 
        
    def delete(self, id):
        print("Mesa " + id + " eliminada")
        mesa = self.mesa_repo.delete(id)
        return mesa       