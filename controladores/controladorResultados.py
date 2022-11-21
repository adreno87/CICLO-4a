from modelos.resultados import Resultados
from repositorios.repositorioResultados import RepositorioResultados

class ResultadosControlador():
    
    def __init__(self):
        print("Creando ControladorResultados")    
        self.repo_resultados = RepositorioResultados()
        
    def getResultados(self):
        resultado = self.repo_resultados.findAll()
        return resultado
    
    def createResultados(self, datosResultados):
        resultado = Resultados(datosResultados)
        datos_salida = self.repo_resultados.save(resultado)
        return datos_salida
    
    def updateResultados(self, id, datosResultados):
        buscar_resultado = self.repo_resultados.findById(id)
        resultado = Resultados(buscar_resultado)
        resultado.totalVotos = datosResultados["total_votos"]
        resultado.ganador = datosResultados["ganador"]
        self.repo_resultados.save(resultado)
        return resultado.__dict__
         
    def deleteResultados(self, id):
        print("resultado " + id + " eliminado")
        resultado = self.repo_resultados.delete(id)
        return resultado 