DROP DATABASE biblioteca_personal
GO

CREATE DATABASE biblioteca_personal
GO

USE biblioteca_personal
GO

CREATE TABLE autor(
	id_autor INT PRIMARY KEY IDENTITY(1,1),
	nombre_autor VARCHAR(30) NOT NULL,
	fecha_nacimiento DATE
)
GO

CREATE TABLE genero(
	id_genero INT PRIMARY KEY IDENTITY(1,1),
	nombre_genero VARCHAR(20) NOT NULL
)
GO

CREATE TABLE libro(
	id_libro INT PRIMARY KEY IDENTITY(1,1),
	titulo_libro VARCHAR(30) NOT NULL,
	id_genero INT NOT NULL,
	id_autor INT NOT NULL
)
GO

CREATE TABLE estado_lectura(
	id_estado_lectura INT PRIMARY KEY IDENTITY(1,1),
	nombre_estado VARCHAR(30) NOT NULL
)
GO

CREATE TABLE lectura(
	id_lectura INT PRIMARY KEY IDENTITY(1,1),
	id_libro INT NOT NULL,
	cant_paginas_leidas INT NOT NULL,
	id_estado_lectura INT NOT NULL
)
GO

CREATE TABLE usuario(
	id_usuario INT PRIMARY KEY IDENTITY(1,1),
	nombre_usuario VARCHAR(30) NOT NULL,
	contrasena VARCHAR(60) NOT NULL,
	rol VARCHAR(10) NOT NULL
)
GO

/*FOREIGN KEYS*/

ALTER TABLE libro ADD CONSTRAINT FK_ID_GENERO FOREIGN KEY (id_genero) REFERENCES genero(id_genero)
GO

ALTER TABLE libro ADD CONSTRAINT FK_ID_AUTOR FOREIGN KEY (id_autor) REFERENCES autor(id_autor)
GO

ALTER TABLE lectura ADD CONSTRAINT FK_ID_LIBRO FOREIGN KEY (id_libro) REFERENCES libro(id_libro)
GO

ALTER TABLE lectura ADD CONSTRAINT FK_ID_ESTADO_LECTURA FOREIGN KEY (id_estado_lectura) REFERENCES estado_lectura(id_estado_lectura)
GO

ALTER TABLE usuario ADD CONSTRAINT DF_ROL DEFAULT 'admin' FOR rol
GO