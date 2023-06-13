INSERT INTO localidad (nombre) VALUES 
    ('Villa Maria'), 
    ('Cordoba'),
    ('Las Varillas'), 
    ('Calchin'), 
    ('Marcos Juarez');


INSERT INTO tipo_documento (nombre) VALUES
    ('DNI'), 
    ('Pasaporte'), 
    ('Libreta Civica');


INSERT INTO direccion (calle, altura, idLocalidad) VALUES
    ('San Martin', 190, 2),
    ('Catamarca', 250, 1),
    ('Julian Alvarez', 55, 4),
    ('Venezuela', 1305, 3),
    ('Santa Fe', 300, 5);


INSERT INTO tipo_producto (nombre) VALUES
    ('Con Receta'),
    ('Venta Libre');


INSERT INTO unidad_medida (nombre) VALUES
    ('Mililitro'),
    ('Miligramo'),
    ('Gramo'),
    ('Unidad');


INSERT INTO producto (nombre, precio, dosis, idUnidadMedida, idTipoProducto) VALUES
    ('Paracetamol', 1500, 650, 2, 2),
    ('Tafirol', 950, 500, 2, 2),
    ('Amoxidal', 2000, 750, 2, 1),
    ('Dentifrico', 300, 150, 1, 2),
    ('Gel de limpieza facial', 2800, 600, 1, 2),
    ('Pañales', 2000, 10, 4, 2);


INSERT INTO proveedor (nombre, telefono, idDireccion) VALUES
    ('Juan Perez', 3533498123, 3),
    ('Martin Lattanzi', 3533498123, 2),
    ('Ignacio Sorti', 3533498123, 1);


INSERT INTO empleado (nombre, telefono, idDireccion) VALUES
    ('Ezequiel Giustinich', 3533458647, 5),
    ('Alejo Sosa', 351409924, 4);