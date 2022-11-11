package seguridad.microservicioseguridad.Controladores;

import seguridad.microservicioseguridad.Modelos.Visualizacion;
import seguridad.microservicioseguridad.Repositorios.RepositorioVisualizacion;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

@CrossOrigin
@RestController
@RequestMapping("/visualizacion")
public class ControladorVisualizacion {
    @Autowired
    private RepositorioVisualizacion miRepositorioVisualizacion;

    @GetMapping("")
    public List<Visualizacion> index(){
        return this.miRepositorioVisualizacion.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Visualizacion create(@RequestBody Visualizacion infoVisualizacion){
        return this.miRepositorioVisualizacion.save(infoVisualizacion);
    }
    @GetMapping("{id}")
    public Visualizacion show(@PathVariable String id){
        Visualizacion visualizacionActual=this.miRepositorioVisualizacion
                .findById(id)
                .orElse(null);
        return visualizacionActual;
    }
    @PutMapping("{id}")
    public Visualizacion update(@PathVariable String id,@RequestBody Visualizacion infoVisualizacion){
        Visualizacion visualizacionActual=this.miRepositorioVisualizacion
                .findById(id)
                .orElse(null);
        if (visualizacionActual!=null){
            visualizacionActual.setNombre(infoVisualizacion.getNombre());
            visualizacionActual.setResultados(infoVisualizacion.getResultados());
            visualizacionActual.setPartido(infoVisualizacion.getPartido());
            return this.miRepositorioVisualizacion.save(visualizacionActual);
        }else{
            return null;
        }
    }
    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Visualizacion visualizacionActual=this.miRepositorioVisualizacion
                .findById(id)
                .orElse(null);
        if (visualizacionActual!=null){
            this.miRepositorioVisualizacion.delete(visualizacionActual);
        }
    }

    public String convertirSHA256(String password) {
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        }
        catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(password.getBytes());
        StringBuffer sb = new StringBuffer();
        for(byte b : hash) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}
