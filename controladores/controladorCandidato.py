from modelos.candidato import Candidato
from modelos.partido import Partido
from repositorios.repositorioCandidato import RepositorioCandidato
from repositorios.RepositorioPartido import RepositorioPartido

class CandidatoControlador():
    
    def __init__(self):
        print("Creando ControladorCandidato")
        self.repo_partido = RepositorioPartido()
        self.repo_candidato = RepositorioCandidato()
        
    """RELACION UNO A MUCHOS --> PARTIDO --> CANDIDATO"""  
    def asignarPartido(self, id, id_partido):
        candidato_actual = Candidato(self.repo_candidato.findById(id))
        partido_actual = Partido(self.repo_partido.findById(id_partido))
        candidato_actual.partido = partido_actual
        return self.repo_candidato.save(candidato_actual)    
        
    def get(self):
        candidatos = self.repo_candidato.findAll()
        return candidatos
    
    def create(self, datosCandidato):
        candidato = Candidato(datosCandidato)
        datos_salida = self.repo_candidato.save(candidato)
        return datos_salida
    
    def find(self, id):
        buscar_candiadto = self.repo_candidato.findById(id)
        candidato = Candidato(buscar_candiadto)
        return candidato.__dict__
    
    def update(self, id, datosCandidato):
        buscar_candiadto = self.repo_candidato.findById(id)
        candidato = Candidato(buscar_candiadto)
        candidato.resolution_number = datosCandidato["resolution_number"]
        candidato.cedula = datosCandidato["cedula"]
        candidato.name = datosCandidato["name"]
        self.repo_candidato.save(candidato)
        return candidato.__dict__
        
    def delete(self, id):
        print("candidato " + id + " eliminado")
        candidato = self.repo_candidato.delete(id) 
        return candidato     