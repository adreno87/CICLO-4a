package seguridad.microservicioseguridad.Repositorios;

import seguridad.microservicioseguridad.Modelos.RolPermiso;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRolPermiso extends MongoRepository<RolPermiso,String> {

}
