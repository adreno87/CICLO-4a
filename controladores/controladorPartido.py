from modelos.partido import Partido
from repositorios.RepositorioPartido import RepositorioPartido

class PartidoControlador():
    
    def __init__(self):
        print("Creando ControladorPartido")    
        self.repo_partido = RepositorioPartido()
        
    def getPartido(self):
        partido = self.repo_partido.findAll()
        return partido
    
    def createPartido(self, datosPartido):
        partido = Partido(datosPartido)
        datos_salida = self.repo_partido.save(partido)
        return datos_salida
    
    def updatePartido(self, id, datosPartido):
        buscar_partido = self.repo_partido.findById(id)
        partido = Partido(buscar_partido)
        partido.name = datosPartido["name"]
        partido.lema = datosPartido["lema"]
        self.repo_partido.save(partido)
        return partido.__dict__
    
        
    def deletePartido(self, id):
        print("partido " + id + " eliminado")
        partido = self.repo_partido.delete(id)
        return partido