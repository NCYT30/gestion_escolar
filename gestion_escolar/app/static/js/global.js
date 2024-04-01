document.addEventListener('DOMContentLoaded', function() {
    var btnCrearAula = document.getElementById('btnCrearAula');
    var modal = document.getElementById('modal');
    var modalTitle = document.getElementById('modal-title');
    var modalForm = document.getElementById('modal-form');

    if (btnCrearAula) {
        btnCrearAula.addEventListener('click', function() {
            modal.style.display = 'block';
            modalTitle.innerText = 'Crear nueva aula';
            modalForm.action = '/aula/create/';
            modalForm.reset();
        });
    }

    var span = document.querySelector('.close');
    if (span) {
        span.addEventListener('click', function() {
            modal.style.display = 'none';
        });
    }

    var editIcons = document.querySelectorAll('.editIcon');
    editIcons.forEach(function(icon) {
        icon.addEventListener('click', function() {
            var aulaId = this.dataset.id;
            modal.style.display = 'block';
            modalTitle.innerText = 'Editar aula';
            modalForm.action = '/aula/update/' + aulaId + '/';
            
            fetch('/aula/obtener_datos_aula/' + aulaId + '/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    // Llenar el formulario con los datos del aula
                    document.getElementById('numero').value = data.numero;
                    document.getElementById('capacidad').value = data.capacidad;
                    document.getElementById('edificio').value = data.edificio;
                    document.getElementById('piso').value = data.piso;
                    document.getElementById('ubicacion').value = data.ubicacion;
                })
                .catch(error => console.error('Error al obtener los datos del aula:', error));
        });
    });
    
});


document.addEventListener('DOMContentLoaded', function() {
    var btnCrearEvento = document.getElementById('btnCrearEvento');
    var modal = document.getElementById('modal_evento');
    var modalTitle = document.getElementById('modal-title');
    var modalForm = document.getElementById('evento-form');

    if (btnCrearEvento) {
        btnCrearEvento.addEventListener('click', function() {
            modal.style.display = 'block';
            modalTitle.innerText = 'Crear nuevo evento';
            modalForm.action = '/evento/create/';
            modalForm.reset();
        });
    }

    var span = modal.querySelector('.close');
    if (span) {
        span.addEventListener('click', function() {
            modal.style.display = 'none';
        });
    }
    

    var editIE = document.querySelectorAll('.editIE');
    editIE.forEach(function(icon) {
        icon.addEventListener('click', function() {
            var eventoId = this.dataset.id;
            modal.style.display = 'block';
            modalTitle.innerText = 'Editar evento';
            modalForm.action = '/evento/update/' + eventoId + '/';
            
            fetch('/evento/obtener_datos_evento/' + eventoId + '/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log(data);
                    // Llenar el formulario con los datos del evento
                    document.getElementById('nombre').value = data.nombre;
                    document.getElementById('descripcion').value = data.descripcion;
                    document.getElementById('fecha').value = data.fecha;
                    document.getElementById('tipo_evento').value = data.tipo_evento;
                    console.log(data.ubicacion); // Verificar que los datos de ubicación se estén recuperando correctamente
                    document.getElementById('ubicacion_evento').setAttribute('value', data.ubicacion);
                    document.getElementById('organizador').value = data.organizador;
                })
                .catch(error => console.error('Error al obtener los datos del evento:', error));
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var deleteForms = document.querySelectorAll('.delete-form');

    deleteForms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevenir el envío del formulario
            var confirmar = confirm("¿Estás seguro de que deseas eliminar este evento?");
            if (confirmar) {
                var url = this.action;
                var formData = new FormData(this);

                fetch(url, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken') // Obtener el token CSRF
                    }
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    var card = this.closest('.card');
                    card.parentNode.removeChild(card);
                })
                .catch(error => console.error('Error al eliminar el evento:', error));
            }
        });
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});



document.addEventListener('DOMContentLoaded', function() {
    var btnCrearAsig = document.getElementById('btnCrearAsig');
    var modal = document.getElementById('modal_asig');
    var modalTitle = document.getElementById('modal-title');
    var modalForm = document.getElementById('asig-form');

    if (btnCrearAsig) {
        btnCrearAsig.addEventListener('click', function() {
            modal.style.display = 'block';
            modalTitle.innerText = 'Crear nueva asignatura';
            modalForm.action = '/asignatura/create/';
            modalForm.reset();

            var span = document.querySelector('.close');
            if (span) {
                span.addEventListener('click', function() {
                    modal.style.display = 'none';
                });
            }
        });
    }

    var editIcons = document.querySelectorAll('.editAsigIcon');
    editIcons.forEach(function(icon) {
        icon.addEventListener('click', function() {
            var AsigId = this.dataset.id;
            modal.style.display = 'block';
            modalTitle.innerText = 'Editar asignatura';
            modalForm.action = '/asignatura/update/' + AsigId + '/';
            
            fetch('/asignatura/obtener_datos_asignatura/' + AsigId + '/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    document.getElementById('nombre_asig').value = data.nombre;
                    document.getElementById('descripcion_asig').value = data.descripcion;
                    document.getElementById('creditos').value = data.creditos;
                })
                .catch(error => console.error('Error al obtener los datos de la asignatura:', error));

            var span = document.querySelector('.close');
            if (span) {
                span.addEventListener('click', function() {
                    modal.style.display = 'none';
                });
            }
        });
    });
    
});


document.addEventListener('DOMContentLoaded', function() {
    var btnCrearProfesor = document.getElementById('btnCrearProfesor');
    var modal = document.getElementById('modal_profesor');
    var modalTitle = document.getElementById('modal-title');
    var modalForm = document.getElementById('profesor-form');

    if (btnCrearProfesor) {
        btnCrearProfesor.addEventListener('click', function() {
            modal.style.display = 'block';
            modalTitle.innerText = 'Crear nuevo profesor';
            modalForm.action = '/profesor/create/';
            modalForm.reset();

            var span = document.querySelector('.close');
            if (span) {
                span.addEventListener('click', function() {
                    modal.style.display = 'none';
                });
            }
        });
    }
});


document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('modal_aisgprofe');
    var modalTitle = document.getElementById('modal-title');
    var modalForm = document.getElementById('asigprofe-form');

    var btnAsigProfe = document.getElementById('btnAsigProfe');
    if (btnAsigProfe) {
        btnAsigProfe.addEventListener('click', function() {
            modal.style.display = 'block';
            modalTitle.innerText = 'Crear nueva asociacion';
            modalForm.action = '/asigprofe/create/';
            modalForm.reset();
        });
    }

    if (modal) {
        var span = modal.querySelector('.close');
        if (span) {
            span.addEventListener('click', function() {
                modal.style.display = 'none';
            });
        }

        var editIsigprofe = document.querySelectorAll('.editIsigprofe');
        editIsigprofe.forEach(function(icon) {
            icon.addEventListener('click', function() {
                var eventoId = this.dataset.id;
                modal.style.display = 'block';
                modalTitle.innerText = 'Editar evento';
                modalForm.action = '/asigprofe/update/' + eventoId + '/';

                fetch('/asigprofe/obtener_datos_asigprofe/' + eventoId + '/')
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.json();
                    })
                    .then(data => {
                        console.log(data);
                        document.getElementById('asignatura').value = data.asignatura;
                        document.getElementById('profesor').value = data.profesor;
                    })
                    .catch(error => console.error('Error al obtener los datos del evento:', error));
            });
        });
    }
});



document.addEventListener('DOMContentLoaded', function() {
    var btnCurso = document.getElementById('btnCurso');
    var modal = document.getElementById('modal_curso');
    var modalTitle = document.getElementById('modal-title');
    var modalForm = document.getElementById('curso-form');

    if (btnCurso) {
        btnCurso.addEventListener('click', function() {
            modal.style.display = 'block';
            modalTitle.innerText = 'Crear nuevo curso';
            modalForm.action = '/curso/create/';
            modalForm.reset();
        });
    }

    var span = modal.querySelector('.close');
    if (span) {
        span.addEventListener('click', function() {
            modal.style.display = 'none';
        });
    }
    

    var editCurso = document.querySelectorAll('.editCurso');
    editCurso.forEach(function(icon) {
        icon.addEventListener('click', function() {
            var eventoId = this.dataset.id;
            modal.style.display = 'block';
            modalTitle.innerText = 'Editar curso';
            modalForm.action = '/curso/update/' + eventoId + '/';
            
            fetch('/curso/obtener_datos_curso/' + eventoId + '/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log(data);
                    document.getElementById('nombre').value = data.nombre;
                    document.getElementById('descripcion').value = data.descripcion;
                    document.getElementById('creditos').value = data.creditos;
                    document.getElementById('ano_academico').value = data.ano_academico;
                    document.getElementById('duracion').value = data.duracion;
                    document.getElementById('requisitos_previos').value = data.requisitos_previos;
                    document.getElementById('materiales_requeridos').value = data.materiales_requeridos;
                    document.getElementById('costo').value = data.costo;
                    document.getElementById('estado').value = data.estado;
                })
                .catch(error => console.error('Error al obtener los datos del evento:', error));
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var btnHorario = document.getElementById('btnHorario');
    var modal = document.getElementById('modal_horario');
    var modalTitle = document.getElementById('modal-title');
    var modalForm = document.getElementById('horario-form');

    if (btnHorario) {
        btnHorario.addEventListener('click', function() {
            modal.style.display = 'block';
            modalTitle.innerText = 'Crear nuevo horario';
            modalForm.action = '/horario/create/';
            modalForm.reset();
        });
    }

    var span = modal.querySelector('.close');
    if (span) {
        span.addEventListener('click', function() {
            modal.style.display = 'none';
        });
    }
    

    var editHorario = document.querySelectorAll('.editHorario');
    editHorario.forEach(function(icon) {
        icon.addEventListener('click', function() {
            var eventoId = this.dataset.id;
            modal.style.display = 'block';
            modalTitle.innerText = 'Editar horario';
            modalForm.action = '/horario/update/' + eventoId + '/';
            
            fetch('/horario/obtener_datos_horario/' + eventoId + '/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log(data);
                    document.getElementById('asignatura').value = data.asignatura;
                    document.getElementById('profesor').value = data.profesor;
                    document.getElementById('dia_semana').value = data.dia_semana;
                    document.getElementById('hora_inicio').value = data.hora_inicio;
                    document.getElementById('hora_fin').value = data.hora_fin;
                    document.getElementById('periodo_academico').value = data.periodo_academico;
                    
                })
                .catch(error => console.error('Error al obtener los datos del evento:', error));
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var btnEstudiante = document.getElementById('btnEstudiante');
    var modal = document.getElementById('modal_estudiante');
    var modalTitle = document.getElementById('modal-title');
    var modalForm = document.getElementById('estudiante-form');

    if (btnEstudiante) {
        btnEstudiante.addEventListener('click', function() {
            modal.style.display = 'block';
            modalTitle.innerText = 'Crear nuevo estudiante';
            modalForm.action = '/estudiantes/create/';
            modalForm.reset();
        });
    }

    var span = modal.querySelector('.close');
    if (span) {
        span.addEventListener('click', function() {
            modal.style.display = 'none';
        });
    }

    var editEstudiante = document.querySelectorAll('.editEstudiante');
    editEstudiante.forEach(function(icon) {
        icon.addEventListener('click', function() {
            var estudianteId = this.dataset.id;
            modal.style.display = 'block';
            modalTitle.innerText = 'Editar estudiante';
            modalForm.action = '/estudiantes/update/' + estudianteId + '/';

            fetch('/estudiantes/obtener_datos_estudiante/' + estudianteId + '/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log(data);
                    document.getElementById('nombre').value = data.nombre;
                    document.getElementById('fecha_nacimiento').value = data.fecha_nacimiento;
                    document.getElementById('direccion').value = data.direccion;
                    document.getElementById('edad').value = data.edad;
                    document.getElementById('genero').value = data.genero;
                    document.getElementById('email').value = data.email;
                    document.getElementById('telefono').value = data.telefono;
                    document.getElementById('fecha_ingreso').value = data.fecha_ingreso;
                    document.getElementById('grado').value = data.grado;
                })
                .catch(error => console.error('Error al obtener los datos del estudiante:', error));
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var btnCalificacion = document.getElementById('btnCalificacion');
    var modal = document.getElementById('modal_calificacion');
    var modalTitle = document.getElementById('modal-title');
    var modalForm = document.getElementById('calificacion-form');

    if (btnCalificacion) {
        btnCalificacion.addEventListener('click', function() {
            modal.style.display = 'block';
            modalTitle.innerText = 'Crear nueva calificacion';
            modalForm.action = '/calificaciones/create/';
            modalForm.reset();
        });
    }

    var span = modal.querySelector('.close');
    if (span) {
        span.addEventListener('click', function() {
            modal.style.display = 'none';
        });
    }

    var editCalificacion = document.querySelectorAll('.editCalificacion');
    editCalificacion.forEach(function(icon) {
        icon.addEventListener('click', function() {
            var calificacionId = this.dataset.id;
            modal.style.display = 'block';
            modalTitle.innerText = 'Editar calificación';
            modalForm.action = '/calificaciones/update/' + calificacionId + '/';
    
            fetch('/calificaciones/obtener_datos_calificacion/' + calificacionId + '/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log(data);
                    document.getElementById('estudiante').value = data.estudiante;
                    document.getElementById('curso').value = data.curso;
                })
                .catch(error => console.error('Error al obtener los datos de la calificación:', error));
        });
    });
});