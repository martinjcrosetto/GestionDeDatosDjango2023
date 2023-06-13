-- WESAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


CREATE DATABASE farmacia;
\c farmacia
-- 1.- UnidadMedida
CREATE TABLE unidad_medida( idUnidadMedida SERIAL,
                            nombre VARCHAR(255),
                            descripcion VARCHAR(255),
                            CONSTRAINT pk_idUnidadMedida PRIMARY KEY (idUnidadMedida)
                            );
-- 1.- Localidad
CREATE TABLE localidad (    idlocalidad SERIAL,
                            nombre VARCHAR(255),
                            codigo_postal VARCHAR(10),
                            CONSTRAINT pk_idLocalidad PRIMARY KEY (idLocalidad)
);

-- 1.- Direccion
CREATE TABLE direccion (    idDireccion SERIAL,
                            calle VARCHAR(255),
                            numero INTEGER,
                            ciudad VARCHAR(255),
                            provincia VARCHAR(255),
                            CONSTRAINT pk_idDireccion PRIMARY KEY (idDireccion)
);
-- 1.- TipoDocumento
CREATE TABLE tipo_documento(    idTipoDocumento SERIAL,
                                nombre VARCHAR(255),
                                CONSTRAINT pk_idTipoDocumento PRIMARY KEY (idTipoDocumento)
);
-- 1.- Proveedor
CREATE TABLE proveedor( idProveedor SERIAL,
                        nombre VARCHAR(255),
                        telefono BIGINT,
                        idDireccion INTEGER,
                        CONSTRAINT pk_idProveedor PRIMARY KEY (idProveedor),
                        CONSTRAINT fk_idDireccion FOREIGN KEY (idDireccion) REFERENCES direccion(idDireccion)
);
-- 1.- ProductoProveedor
CREATE TABLE producto_proveedor(idProductoProveedor SERIAL,
                                idProducto INTEGER,
                                idProveedor INTEGER,
                                precio DECIMAL(10, 2),
                                cantidad INTEGER,
                                PRIMARY KEY (idProductoProveedor),
                                CONSTRAINT fk_productoProveedorProducto FOREIGN KEY (idProducto) REFERENCES producto(idProducto),
                                CONSTRAINT fk_productoProveedorProveedor FOREIGN KEY (idProveedor) REFERENCES proveedor(idProveedor)
);
-- 1.- Empleado
CREATE TABLE empleado(  idEmpleado SERIAL,
                        nombre VARCHAR(255),
                        telefono BIGINT,
                        idDireccion INTEGER,
                        CONSTRAINT pk_idEmpleado PRIMARY KEY (idEmpleado),
                        CONSTRAINT pk_idDireccion FOREIGN KEY (idDireccion) REFERENCES direccion(idDireccion)
);
-- 1.- Producto
CREATE TABLE producto(  idProducto SERIAL,
                        nombre VARCHAR(255),
                        idTipoProducto INTEGER,
                        idUnidadMedida INTEGER,
                        dosis INTEGER,
                        precio DECIMAL(10, 2),
                        PRIMARY KEY (idProducto),
                        CONSTRAINT fk_idTipoProducto FOREIGN KEY (idTipoProducto) REFERENCES tipoProducto(idTipoProducto),
                        CONSTRAINT fk_idUnidadMedida FOREIGN KEY (idUnidadMedida) REFERENCES unidadMedida(idUnidadMedida)
);
-- 1.- TipoProducto
CREATE TABLE tipo_producto( idTipoProducto SERIAL,
                            nombre VARCHAR(255),
                            CONSTRAINT pk_idTipoProducto PRIMARY KEY (idTipoProducto)
);

-- 1.- Venta
CREATE TABLE venta( idVenta SERIAL,
                    idEmpleado INTEGER,
                    fecha DATE,
                    hora TIME,
                    CONSTRAINT fk_idEmpleado FOREIGN KEY (idEmpleado) REFERENCES empleado(idEmpleado)
);
-- 1.- DetalleVenta
CREATE TABLE detalle_venta( idDetalleVenta SERIAL,
                            idVenta INTEGER,
                            idProducto INTEGER,
                            cantidad INTEGER,
                            precioUnitario DECIMAL(10, 2),                    
                            CONSTRAINT pk_idDetalleVenta PRIMARY KEY (idDetalleVenta),
                            CONSTRAINT fk_idVenta FOREIGN KEY (idVenta) REFERENCES venta(idVenta),
                            CONSTRAINT fk_idProducto FOREIGN KEY (idProducto) REFERENCES producto(idProducto)
);












