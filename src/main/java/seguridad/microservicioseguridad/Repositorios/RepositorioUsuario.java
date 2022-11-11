package seguridad.microservicioseguridad.Repositorios;
import seguridad.microservicioseguridad.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioUsuario extends
        MongoRepository<Usuario,String> {
}