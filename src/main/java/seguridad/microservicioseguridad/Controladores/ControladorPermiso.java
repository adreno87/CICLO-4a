package seguridad.microservicioseguridad.Controladores;

import seguridad.microservicioseguridad.Modelos.Permiso;
import seguridad.microservicioseguridad.Repositorios.RepositorioPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class ControladorPermiso {
    @Autowired
    RepositorioPermiso miRepositorioPermiso;

    @GetMapping("/permisos/listar")
    public List<Permiso>listarPermisos(){
        return this.miRepositorioPermiso.findAll();
    }
    @PostMapping("/permisos/crear")
    public Permiso crearPermiso(@RequestBody Permiso rolEntrada){
        return this.miRepositorioPermiso.save(rolEntrada);
    }

    @DeleteMapping("permisos/eliminar/{idPermiso}")
    public String eliminarPermiso(@PathVariable String idPermiso){
        miRepositorioPermiso.deleteById(idPermiso);
        return "el permiso de ha eliminado";
    }

    @PutMapping("permisos/actualizar/{idPermiso}")
    public String actualizarPermiso(@PathVariable String idPermiso,
                                    @RequestBody Permiso permisoEntrada){
        Permiso permisoConsulta = miRepositorioPermiso.findById(idPermiso).orElse(null);
        permisoConsulta.setMetodo(permisoEntrada.getMetodo());
        permisoConsulta.setUrl(permisoEntrada.getUrl());
        miRepositorioPermiso.save(permisoConsulta);
        return "el permiso se ha actualizado";
    }
}
