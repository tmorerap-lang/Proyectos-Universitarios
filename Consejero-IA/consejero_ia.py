// ─────────────────────────────────────────────
// ───── NAVEGACIÓN ENTRE PANTALLAS ─────────────
// ─────────────────────────────────────────────

onEvent("btnInicio", "click", function() {
  setScreen("pantallaMenu");
});

onEvent("btnRecordatorios", "click", function() {
  setScreen("pantallaRecordatorios");
});

onEvent("btnConsejoEmocional", "click", function() {
  setScreen("pantallaConsejo");
});

onEvent("btnEstres", "click", function() {
  setScreen("pantallaEstres");
});

onEvent("btnTareas", "click", function() {
  setScreen("pantallaTareas");
});

// Volver desde subpantallas al menú
onEvent("btnVolverRecordatorios", "click", function() {
  setScreen("pantallaMenu");
});
onEvent("btnVolverConsejo", "click", function() {
  setScreen("pantallaMenu");
});
onEvent("btnVolverEstres", "click", function() {
  setScreen("pantallaMenu");
});
onEvent("btnVolverTareas", "click", function() {
  setScreen("pantallaMenu");
});

// ─────────────────────────────────────────────
// ───── CONSEJOS EMOCIONALES ──────────────────
// ─────────────────────────────────────────────

var consejos = [
  "Respira profundo, estás haciendo lo mejor que puedes.",
  "Recuerda descansar, tu bienestar es primero.",
  "Organiza tus tareas en pequeños pasos.",
  "Tómate 5 minutos para relajarte.",
  "Vas muy bien, sigue avanzando poco a poco."
];

onEvent("btnConsejo", "click", function() {
  var n = randomNumber(0, consejos.length - 1);
  setText("txtConsejo", consejos[n]);
});

// ─────────────────────────────────────────────
// ───── RECORDATORIOS ─────────────────────────
// ─────────────────────────────────────────────

var listaRecordatorios = [];

onEvent("btnAgregarRecordatorio", "click", function() {
  var rec = getText("txtRecordatorio");

  if (rec !== "") {
    appendItem(listaRecordatorios, rec);
    setText("listaRecordatorios", listaRecordatorios.join("\n"));
    setText("txtRecordatorio", "");
  }
});

// ─────────────────────────────────────────────
// ───── NIVEL DE ESTRÉS ───────────────────────
// ─────────────────────────────────────────────

onEvent("btnEvaluarEstres", "click", function() {
  var nivel = getNumber("sliderEstres");

  if (nivel <= 2) {
    setText("txtResultadoEstres", "Estás tranquilo. ¡Sigue así!");
  } 
  else if (nivel == 3) {
    setText("txtResultadoEstres", "Nivel moderado. Toma un respiro.");
  } 
  else {
    setText("txtResultadoEstres", "Alto estrés. Haz una pausa y respira profundo.");
  }
});

// ─────────────────────────────────────────────
// ───── TAREAS ────────────────────────────────
// ─────────────────────────────────────────────

var listaTareas = [];

onEvent("btnAgregarTarea", "click", function() {
  var tarea = getText("txtTarea");
  var hora = getText("txtHora");
  var prioridad = getText("dropdownPrioridad");

  if (tarea !== "" && hora !== "" && prioridad !== "") {
    var texto = tarea + " - " + hora + " - " + prioridad;
    appendItem(listaTareas, texto);

    setText("listaTareas", listaTareas.join("\n"));
    setText("txtTarea", "");
    setText("txtHora", "");
  }
});

// Botón para ir a la pantalla de inicio
onEvent("btnSalir", "click", function() {
  setScreen("pantallaInicio");
});

// ─────────────────────────────────────────────
// ───── REGISTRO E INICIO DE SESIÓN ───────────
// ─────────────────────────────────────────────

// Aquí se guarda temporalmente el usuario
var usuarioRegistrado = {
  correo: "",
  contrasena: ""
};

// Ir al registro desde pantallaInicio
onEvent("btnIrRegistro", "click", function() {
  setScreen("pantallaRegistro");
});

// Ir al Login desde el registro
onEvent("btnIrLoginDesdeRegistro", "click", function() {
  setScreen("pantallaLogin");
});

// Ir al Registro desde el login
onEvent("btnIrRegistroDesdeLogin", "click", function() {
  setScreen("pantallaRegistro");
});

// Volver al inicio desde registro
onEvent("btnVolverRegistro", "click", function() {
  setScreen("pantallaInicio");
});

// Volver al inicio desde login
onEvent("btnVolverLogin", "click", function() {
  setScreen("pantallaInicio");
});

// ───── REGISTRAR USUARIO ─────────────────────

onEvent("btnRegistrarUsuario", "click", function() {

  var correo = getText("inputCorreoRegistro");
  var clave = getText("inputContrasenaRegistro");

  if (correo === "" || clave === "") {
    setText("lblRegistroEstado", "Completa todos los campos.");
    return;
  }

  if (!(correo.includes("@") && correo.includes("."))) {
    setText("lblRegistroEstado", "Ingresa un correo válido.");
    return;
  }

  if (clave.length < 6) {
    setText("lblRegistroEstado", "La contraseña debe tener al menos 6 caracteres.");
    return;
  }

  // Guardar usuario
  usuarioRegistrado.correo = correo;
  usuarioRegistrado.contrasena = clave;

  setText("lblRegistroEstado", "Registro exitoso. Ahora inicia sesión.");

  setText("inputCorreoRegistro", "");
  setText("inputContrasenaRegistro", "");
});

// ───── INICIO DE SESIÓN ───────────────────────

onEvent("btnIniciarSesion", "click", function() {

  var correo = getText("inputCorreoLogin");
  var clave = getText("inputContrasenaLogin");

  if (usuarioRegistrado.correo === "") {
    setText("lblLoginEstado", "No hay usuarios registrados.");
    return;
  }

  if (correo === usuarioRegistrado.correo &&
      clave === usuarioRegistrado.contrasena) {

    setText("lblLoginEstado", "Inicio de sesión exitoso.");
    setScreen("pantallaMenu");

  } else {
    setText("lblLoginEstado", "Correo o contraseña incorrectos.");
  }

  setText("inputCorreoLogin", "");
  setText("inputContrasenaLogin", "");
});

