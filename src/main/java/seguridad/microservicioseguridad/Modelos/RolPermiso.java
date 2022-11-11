package seguridad.microservicioseguridad.Modelos;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document()
public class RolPermiso {

    @Id
    private String _id;
    @DBRef
    private Rol _idRol;
    @DBRef
    private Permiso _idPermiso;

    public RolPermiso(Rol _idRol, Permiso _idPermiso) {
        this._idRol = _idRol;
        this._idPermiso = _idPermiso;
    }

    public Rol get_idRol() {
        return _idRol;
    }

    public void set_idRol(Rol _idRol) {
        this._idRol = _idRol;
    }

    public Permiso get_idPermiso() {
        return _idPermiso;
    }

    public void set_idPermiso(Permiso _idPermiso) {
        this._idPermiso = _idPermiso;
    }
}
