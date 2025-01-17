package utn.estudiantes.servicio;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import utn.estudiantes.modelo.Estudiantes2024;
import utn.estudiantes.repositorio.EstudianteRepositorio;

import java.util.List;

@Service
public class EstudianteServicio implements IEstudianteServicio{
    @Autowired
    private EstudianteRepositorio estudianteRepositorio;

    @Override
    public List<Estudiantes2024> listarEstudiantes() {
        List<Estudiantes2024> estudiantes = estudianteRepositorio.findAll();
        return estudiantes;
    }

    @Override
    public Estudiantes2024 buscarEstudiantePorId(Integer idEstudiantes2024) {
        Estudiantes2024 estudiante = estudianteRepositorio.findById(idEstudiantes2024).orElse(null);
        return estudiante;
    }

    @Override
    public void guardarEstudiante(Estudiantes2024 estudiante) {
        estudianteRepositorio.save(estudiante);
    }

    @Override
    public void eliminarEstudiante(Estudiantes2024 estudiante) {
        estudianteRepositorio.delete(estudiante);
    }
}
