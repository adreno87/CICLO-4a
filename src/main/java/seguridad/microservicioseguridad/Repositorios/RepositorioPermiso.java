package seguridad.microservicioseguridad.Repositorios;

import seguridad.microservicioseguridad.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermiso extends MongoRepository<Permiso,String> {

}
