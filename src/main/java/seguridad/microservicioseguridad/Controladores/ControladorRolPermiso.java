package seguridad.microservicioseguridad.Controladores;

import seguridad.microservicioseguridad.Modelos.Permiso;
import seguridad.microservicioseguridad.Modelos.Rol;
import seguridad.microservicioseguridad.Modelos.RolPermiso;
import seguridad.microservicioseguridad.Repositorios.RepositorioPermiso;
import seguridad.microservicioseguridad.Repositorios.RepositorioRol;
import seguridad.microservicioseguridad.Repositorios.RepositorioRolPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/rolpermiso")
public class ControladorRolPermiso {
    @Autowired
    RepositorioPermiso miRepoPermiso;
    @Autowired
    RepositorioRol miRepoRol;
    @Autowired
    RepositorioRolPermiso miRepoRolPermiso;

    @PostMapping("/crear/{idRol}/permiso/{idPermiso}")
    public RolPermiso crearRolPermiso(@PathVariable String idRol, @PathVariable String idPermiso){
        Rol rolConsulta = miRepoRol.findById(idRol).orElse(null);
        Permiso permisoConsulta = miRepoPermiso.findById(idPermiso).orElse(null);
        RolPermiso rolPermiso = new RolPermiso(rolConsulta,permisoConsulta);
        return miRepoRolPermiso.save(rolPermiso);
    }

    @GetMapping("/listar")
    public List<RolPermiso> listarRolPermiso(){
        return miRepoRolPermiso.findAll();
    }

    @PutMapping("/actualizar/{idRol}/permiso/{idPermiso}")
    public void asignarRolPermiso(){

    }

    @DeleteMapping("/eliminar/{idRolPermiso}")
    public void eliminarRolPermiso(){

    }

    @GetMapping("validar-permiso/rol/{id_rol}")
    public RolPermiso getPermiso(@PathVariable String id_rol, @RequestBody Permiso infoPermiso) {
        Permiso elPermiso = this.miRepoPermiso.getPermiso(infoPermiso.getUrl(), infoPermiso.getMetodo());
        Rol elRol = this.miRepoRol.findById(id_rol).get();
        if (elPermiso != null && elRol != null) {
            return this.miRepoRolPermiso.getPermisoRol(elRol.get_id(), elPermiso.get_id());
        } else {
            return null;
        }
    }
}
