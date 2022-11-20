package seguridad.microservicioseguridad.Repositorios;

import seguridad.microservicioseguridad.Modelos.RolPermiso;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioRolPermiso extends MongoRepository<RolPermiso,String> {
    @Query("{'rol.$id': ObjectId(?0),'permiso.$id': ObjectId(?1)}")
    RolPermiso getPermisoRol(String id_rol, String id_permiso);
}
