package seguridad.microservicioseguridad.Controladores;

import seguridad.microservicioseguridad.Modelos.Permiso;
import seguridad.microservicioseguridad.Modelos.Rol;
import seguridad.microservicioseguridad.Modelos.RolPermiso;
import seguridad.microservicioseguridad.Repositorios.RepositorioPermiso;
import seguridad.microservicioseguridad.Repositorios.RepositorioRol;
import seguridad.microservicioseguridad.Repositorios.RepositorioRolPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/rolpermiso")
public class ControladorRolPermiso {
    @Autowired
    private RepositorioRolPermiso miRepoRolPermiso;
    @Autowired
    private RepositorioPermiso miRepoPermiso;
    @Autowired
    private RepositorioRol miRepoRol;

    @GetMapping("")
    public List<RolPermiso> index(){
        return this.miRepoRolPermiso.findAll();
    }
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("rol/{id_rol}/permiso/{id_permiso}")
    public RolPermiso create(@PathVariable String id_rol,@PathVariable
    String id_permiso) {
        RolPermiso nuevo = new RolPermiso();
        Rol elRol = this.miRepoRol.findById(id_rol).get();
        Permiso elPermiso = this.miRepoPermiso.findById(id_permiso).get();
        if (elRol != null && elPermiso != null) {
            nuevo.set_idPermiso(elPermiso);
            nuevo.set_idRol(elRol);
            return this.miRepoRolPermiso.save(nuevo);
        } else {
            return null;
        }
    }
    @GetMapping("{id}")
    public RolPermiso show(@PathVariable String id) {
        RolPermiso permisosRolesActual = this.miRepoRolPermiso
                .findById(id)
                .orElse(null);
        return permisosRolesActual;
    }
    @PutMapping("{id}/rol/{id_rol}/permiso/{id_permiso}")
    public RolPermiso update(@PathVariable String id,@PathVariable
    String id_rol,@PathVariable String id_permiso){
        RolPermiso permisosRolesActual=this.miRepoRolPermiso
                .findById(id)
                .orElse(null);
        Rol elRol=this.miRepoRol.findById(id_rol).get();
        Permiso
                elPermiso=this.miRepoPermiso.findById(id_permiso).get();
        if(permisosRolesActual!=null && elPermiso!=null && elRol!=null){
            permisosRolesActual.set_idPermiso(elPermiso);
            permisosRolesActual.set_idRol(elRol);
            return
                    this.miRepoRolPermiso.save(permisosRolesActual);
        }else{
            return null;
        }
    }
    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        RolPermiso permisosRolesActual=this.miRepoRolPermiso
                .findById(id)
                .orElse(null);
        if (permisosRolesActual!=null){
            this.miRepoRolPermiso.delete(permisosRolesActual);
        }
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
