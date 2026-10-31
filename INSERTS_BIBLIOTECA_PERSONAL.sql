USE biblioteca_personal;

/* ===== AUTOR ===== */
INSERT INTO autor (nombre_autor, fecha_nacimiento) VALUES
('Gabriel García Márquez', '1927-03-06'),
('Mario Vargas Llosa', '1936-03-28'),
('Isabel Allende', '1942-08-02'),
('Julio Cortázar', '1914-08-26'),
('Jorge Luis Borges', '1899-08-24'),
('Stephen King', '1947-09-21'),
('Agatha Christie', '1890-09-15'),
('J.R.R. Tolkien', '1892-01-03'),
('Isaac Asimov', '1920-01-02'),
('Ray Bradbury', '1920-08-22');

/* ===== GENERO ===== */
INSERT INTO genero (nombre_genero) VALUES
('Novela'),
('Cuento'),
('Fantasía'),
('Ciencia ficción'),
('Terror'),
('Misterio'),
('Realismo mágico');

/* ===== ESTADO_LECTURA ===== */
INSERT INTO estado_lectura (nombre_estado) VALUES
('Pendiente'),
('Leyendo'),
('Terminado'),
('Abandonado');

/* ===== LIBRO (titulo, id_genero, id_autor) ===== */
INSERT INTO libro (titulo_libro, id_genero, id_autor) VALUES
('Cien años de soledad', 7, 1),
('Relato de un náufrago', 1, 1),
('La ciudad y los perros', 1, 2),
('Conversación en La Catedral', 1, 2),
('La casa de los espíritus', 7, 3),
('Rayuela', 1, 4),
('Bestiario', 2, 4),
('Ficciones', 2, 5),
('El Aleph', 2, 5),
('It', 5, 6),
('El resplandor', 5, 6),
('Asesinato en el Orient Express', 6, 7),
('El señor de los anillos', 3, 8),
('Fundación', 4, 9),
('Fahrenheit 451', 4, 10),
('Crónicas marcianas', 4, 10);

/* ===== LECTURA (id_libro, cant_paginas_leidas, id_estado_lectura) ===== */
INSERT INTO lectura (id_libro, cant_paginas_leidas, id_estado_lectura) VALUES
(1, 471, 3),
(2, 120, 3),
(3, 350, 3),
(4, 200, 2),
(5, 433, 3),
(6, 90, 4),
(7, 0, 1),
(8, 180, 3),
(9, 150, 2),
(10, 600, 2),
(11, 447, 3),
(12, 256, 3),
(13, 320, 2),
(14, 0, 1),
(15, 158, 3),
(16, 40, 4);