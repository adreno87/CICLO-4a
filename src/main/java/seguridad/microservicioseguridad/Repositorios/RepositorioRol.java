package seguridad.microservicioseguridad.Repositorios;

import seguridad.microservicioseguridad.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Rol,String> {

}
