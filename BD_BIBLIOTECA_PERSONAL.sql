CREATE DATABASE IF NOT EXISTS biblioteca_personal CHARACTER SET 'utf8mb4';

USE biblioteca_personal;

CREATE TABLE autor(
	id_autor INT PRIMARY KEY AUTO_INCREMENT,
	nombre_autor VARCHAR(30) NOT NULL UNIQUE,
	fecha_nacimiento DATE
);

CREATE TABLE genero(
	id_genero INT PRIMARY KEY AUTO_INCREMENT,
	nombre_genero VARCHAR(20) NOT NULL
);

CREATE TABLE libro(
	id_libro INT PRIMARY KEY AUTO_INCREMENT,
	titulo_libro VARCHAR(40) NOT NULL,
	id_genero INT NOT NULL,
	id_autor INT NOT NULL
);

CREATE TABLE estado_lectura(
	id_estado_lectura INT PRIMARY KEY AUTO_INCREMENT,
	nombre_estado VARCHAR(30) NOT NULL
);

CREATE TABLE lectura(
	id_lectura INT PRIMARY KEY AUTO_INCREMENT,
	id_libro INT NOT NULL,
	cant_paginas_leidas INT NOT NULL,
	id_estado_lectura INT NOT NULL
);

CREATE TABLE usuario(
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
	nombre_usuario VARCHAR(30) NOT NULL,
	contrasena VARCHAR(255) NOT NULL,
	rol VARCHAR(10) NOT NULL DEFAULT 'admin'
);

/*FOREIGN KEYS*/

ALTER TABLE libro ADD CONSTRAINT FK_ID_GENERO FOREIGN KEY (id_genero) REFERENCES genero(id_genero);

ALTER TABLE libro ADD CONSTRAINT FK_ID_AUTOR FOREIGN KEY (id_autor) REFERENCES autor(id_autor);

ALTER TABLE lectura ADD CONSTRAINT FK_ID_LIBRO FOREIGN KEY (id_libro) REFERENCES libro(id_libro);

ALTER TABLE lectura ADD CONSTRAINT FK_ID_ESTADO_LECTURA FOREIGN KEY (id_estado_lectura) REFERENCES estado_lectura(id_estado_lectura);