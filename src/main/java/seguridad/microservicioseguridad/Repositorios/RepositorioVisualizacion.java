package seguridad.microservicioseguridad.Repositorios;

import seguridad.microservicioseguridad.Modelos.Visualizacion;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioVisualizacion extends MongoRepository<Visualizacion,String> {

}
