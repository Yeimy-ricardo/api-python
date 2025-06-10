"use strict";
//caso de uso registro y validacion
class Usuario {
    constructor(nombre, correo, contrasena) {
        this.nombre = nombre;
        this.correo = correo;
        this.contrasena = contrasena;
    }
}
const usuarios = [];
function registrar(nombre, correo, contrasena) {
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
function login(nombreOCorreo, contrasena) {
    const usuario = usuarios.find(u => (u.nombre === nombreOCorreo || u.correo === nombreOCorreo) && u.contrasena === contrasena);
    if (usuario) {
        console.log(`Bienvenido, ${usuario.nombre}`);
    }
    else {
        console.log("Usuario o contraseña incorrectos.");
    }
}
// Pruebas rápidas
registrar("pepe", "pepe@mail.com", "clave123");
registrar("pepe", "otro@mail.com", "clave456"); // repetido
registrar("ana", "ana@mail.com", "123"); // contraseña corta
login("pepe", "clave123"); // correcto
login("pepe@mail.com", "clave123"); // también válido
login("ana", "123"); // incorrecto
