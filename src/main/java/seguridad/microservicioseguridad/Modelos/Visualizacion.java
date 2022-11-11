package seguridad.microservicioseguridad.Modelos;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
@Data
@Document()
public class Visualizacion {
    @Id
    private String _id;
    private String nombre;
    private String resultados;
    private String partido;

    public Visualizacion(String nombre, String resultados, String partido) {
        this.nombre = nombre;
        this.resultados = resultados;
        this.partido = partido;
    }

    public String get_id() {
        return _id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getResultados() {
        return resultados;
    }

    public void setResultados(String resultados) {
        this.resultados = resultados;
    }

    public String getPartido() {
        return partido;
    }

    public void setPartido(String partido) {
        this.partido = partido;
    }
}
