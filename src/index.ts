//caso de uso registro y validacion
class Usuario {
  constructor(
    public nombre: string,
    public correo: string,
    public contrasena: string
  ) {}
}

const usuarios: Usuario[] = [];

function registrar(nombre: string, correo: string, contrasena: string): void {
  // Validar duplicados
  const yaExiste = usuarios.some(u => u.nombre === nombre || u.correo === correo);
  if (yaExiste) {
    console.log("Ya existe un usuario con ese nombre o correo.");
    return;
  }

  // Validar contraseña
  if (contrasena.length < 6) {
    console.log("La contraseña debe tener al menos 6 caracteres.");
    return;
  }

  usuarios.push(new Usuario(nombre, correo, contrasena));
  console.log("Usuario registrado con éxito.");
}

function login(nombreOCorreo: string, contrasena: string): void {
  const usuario = usuarios.find(
    u => (u.nombre === nombreOCorreo || u.correo === nombreOCorreo) && u.contrasena === contrasena
  );

  if (usuario) {
    console.log(`Bienvenido, ${usuario.nombre}`);
  } else {
    console.log("Usuario o contraseña incorrectos.");
  }
}

// Pruebas rápidas
registrar("lio", "lilo@mail.com", "clave123");
registrar("lilo", "pepe@mail.com", "clave456"); // repetido
registrar("ana", "ana@mail.com", "123"); // contraseña corta

login("luis", "clave123"); // correcto
login("luis@mail.com", "clave123"); // también válido
login("ana", "123"); // incorrecto


