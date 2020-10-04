-- Database: minimarket

-- DROP DATABASE minimarket;

CREATE DATABASE minimarket
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- ######################################
-- ######## Esquema de Roles ############
-- ######################################

-- roles
-- Table: public.roles

-- DROP TABLE public.roles;

CREATE TABLE public.roles
(
    id_rol SERIAL, --('roles_id_rol_seq'::regclass),
    nombre character varying(150) COLLATE pg_catalog."default",
    contrasena character varying(150) COLLATE pg_catalog."default",
    cargo character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT roles_pkey PRIMARY KEY (id_rol)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.roles
    OWNER to postgres;

-- POR FAVOR COLOCAR LA SENTENCIA SIGUIENTE
-- Esto va generar un usuario administrado, cuyos datos seran:
-- usuario: admin
-- contraseña: password
-- cargo: admin
-- Esto para poder utilizar bien el programa, y se puede registrar más usuarios con cargo admin o lector.

INSERT INTO roles (nombre, contrasena, cargo) VALUES
('admin', 'password', 'admin')

-- ######################################
-- ############# Tablas #################
-- ######################################


-- TABLAS
-- categoria_frutas

-- Table: public.categoria_frutas

-- DROP TABLE public.categoria_frutas;

CREATE TABLE public.categoria_frutas
(
    id_producto SERIAL, --('categoria_frutas_id_producto_seq'::regclass),
    codigo character varying(150) COLLATE pg_catalog."default",
    producto character varying(150) COLLATE pg_catalog."default",
    precio_por_unidad decimal,
    cantidad integer,
    CONSTRAINT categoria_frutas_pkey PRIMARY KEY (id_producto)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.categoria_frutas
    OWNER to postgres;

-- categoria_frutas
-- Table: public.categoria_frutas

-- DROP TABLE public.categoria_frutas;


-- TABLAS
-- categoria_verduras

-- Table: public.categoria_verduras

-- DROP TABLE public.categoria_verduras;

CREATE TABLE public.categoria_verduras
(
    id_producto SERIAL, --('categoria_verduras_id_producto_seq'::regclass),
    codigo character varying(150) COLLATE pg_catalog."default",
    producto character varying(150) COLLATE pg_catalog."default",
    precio_por_unidad decimal,
    cantidad integer,
    CONSTRAINT categoria_verduras_pkey PRIMARY KEY (id_producto)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.categoria_verduras
    OWNER to postgres;

-- categoria_verduras
-- Table: public.categoria_verduras

-- DROP TABLE public.categoria_verduras;


-- TABLAS
-- categoria_abarrotes

-- Table: public.categoria_abarrotes

-- DROP TABLE public.categoria_abarrotes;

CREATE TABLE public.categoria_abarrotes
(
    id_producto SERIAL, --('categoria_abarrotes_id_producto_seq'::regclass),
    codigo character varying(150) COLLATE pg_catalog."default",
    producto character varying(150) COLLATE pg_catalog."default",
    precio_por_unidad decimal,
    cantidad integer,
    CONSTRAINT categoria_abarrotes_pkey PRIMARY KEY (id_producto)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.categoria_abarrotes
    OWNER to postgres;

-- categoria_abarrotes
-- Table: public.categoria_abarrotes

-- DROP TABLE public.categoria_abarrotes;


-- TABLAS
-- almacen

-- Table: public.almacen

-- DROP TABLE public.almacen;

CREATE TABLE public.almacen
(
    id_almacen SERIAL, --('almacen_id_almacen_seq'::regclass),
    codigo character varying(150) COLLATE pg_catalog."default",
    producto character varying(150) COLLATE pg_catalog."default",
    precio_por_unidad decimal,
    cantidad integer,
    categoria character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT almacen_pkey PRIMARY KEY (id_almacen)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.almacen
    OWNER to postgres;

-- almacen
-- Table: public.almacen

-- DROP TABLE public.almacen;

CREATE TABLE public.ventas
(
    id_ventas SERIAL, --('ventas_id_ventas_seq'::regclass),
    dni character varying(150) COLLATE pg_catalog."default",
    producto character varying(150) COLLATE pg_catalog."default",
    cantidad_comprada integer,
    precio_total decimal,
    fecha character varying(150) COLLATE pg_catalog."default",
    mes_venta character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT ventas_pkey PRIMARY KEY (id_ventas)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.ventas
    OWNER to postgres;

-- ventas
-- Table: public.ventas

-- DROP TABLE public.ventas;