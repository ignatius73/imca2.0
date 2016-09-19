-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.1.16-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Volcando estructura de base de datos para imca
CREATE DATABASE IF NOT EXISTS `imca` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `imca`;


-- Volcando estructura para tabla imca.alumnos
CREATE TABLE IF NOT EXISTS `alumnos` (
  `idAlumnos` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  `Apellido` varchar(255) DEFAULT NULL,
  `DNI` bigint(20) NOT NULL,
  `Nacionalidad` int(10) unsigned DEFAULT NULL,
  `Fecha_Nacimiento` date DEFAULT NULL,
  `Edad` int(10) unsigned DEFAULT NULL,
  `Domicilio` varchar(255) DEFAULT NULL,
  `Localidad` varchar(255) NOT NULL,
  `Partido` varchar(255) NOT NULL,
  `CP` varchar(30) DEFAULT NULL,
  `Telefono` int(10) unsigned DEFAULT NULL,
  `Celular` int(10) unsigned DEFAULT NULL,
  `Estudios_Cursados` int(10) unsigned DEFAULT NULL,
  `Otros` varchar(255) DEFAULT NULL,
  `Trabaja` tinyint(1) DEFAULT NULL,
  `Ocupacion` varchar(255) DEFAULT NULL,
  `Grupo_Sanguineo` varchar(45) DEFAULT NULL,
  `Antitetanica` tinyint(1) DEFAULT NULL,
  `Presion_Arterial` float DEFAULT NULL,
  `Enfermedades` varchar(255) DEFAULT NULL,
  `Tratamiento` tinyint(1) DEFAULT NULL,
  `alergias` varchar(255) DEFAULT NULL,
  `emergencias` varchar(255) DEFAULT NULL,
  `osocial` varchar(255) DEFAULT NULL,
  `foto` blob,
  PRIMARY KEY (`idAlumnos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla imca.alumnos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `alumnos` DISABLE KEYS */;
/*!40000 ALTER TABLE `alumnos` ENABLE KEYS */;


-- Volcando estructura para tabla imca.asignaturas
CREATE TABLE IF NOT EXISTS `asignaturas` (
  `id_asignatura` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `carrera` varchar(255) NOT NULL,
  `correlativas` text COMMENT 'igual a id_asignaturas',
  `horario` text,
  `vacantes` text,
  `anio` tinyint(4) DEFAULT NULL,
  `cursada_paralela` int(11) DEFAULT NULL COMMENT 'igual a id_asignatura',
  PRIMARY KEY (`id_asignatura`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla imca.asignaturas: ~55 rows (aproximadamente)
/*!40000 ALTER TABLE `asignaturas` DISABLE KEYS */;
REPLACE INTO `asignaturas` (`id_asignatura`, `nombre`, `carrera`, `correlativas`, `horario`, `vacantes`, `anio`, `cursada_paralela`) VALUES
	(1, 'DIBUJO', '1', NULL, NULL, NULL, 0, NULL),
	(2, 'PINTURA (TECNOLOGÍA)', '1', NULL, NULL, NULL, 0, NULL),
	(3, 'ESCULTURA CERAMICA (MODELADO)', '1', NULL, NULL, NULL, 0, NULL),
	(4, 'ARTES DEL FUEGO I (DECORACIÓN)', '1', NULL, NULL, NULL, 0, NULL),
	(5, 'ARTES DEL FUEGO II (ALFARERÍA)', '1', NULL, NULL, NULL, 0, NULL),
	(6, 'LENGUAJE VISUAL', '1', NULL, NULL, NULL, 0, NULL),
	(7, 'HISTORIA DEL ARTE Y LA CULTURA', '1', NULL, NULL, NULL, 0, NULL),
	(8, 'INTRODUCCIÓN AL ANÁLISIS', '1', NULL, NULL, NULL, 0, NULL),
	(9, 'DIBUJO I', '5', NULL, NULL, NULL, 1, NULL),
	(10, 'QUÍMICA APLICADA I', '5', NULL, NULL, NULL, 1, NULL),
	(11, 'ALFARERÍA', '2', NULL, NULL, NULL, 1, NULL),
	(12, 'MOLDERÍA I', '2', NULL, NULL, NULL, 1, NULL),
	(13, 'LENGUAJE VISUAL I', '5', NULL, NULL, NULL, 1, NULL),
	(14, 'HISTORIA DEL ARTE I/HISTORIA DE LAS ARTES VISUALES', '5', NULL, NULL, NULL, 1, NULL),
	(15, 'CERÁMICA (MODELADO/DECORACIÓN)', '2', NULL, NULL, NULL, 1, NULL),
	(16, 'PROYECTO Y DISEÑO CERÁMICO I/DIBUJO II', '5', '9,13', NULL, NULL, 2, NULL),
	(17, 'TECNOLOGÍA APLICADA A LA CERÁMICA I', '5', '29,10', NULL, NULL, 2, NULL),
	(18, 'MOLDERÍA II', '2', NULL, NULL, NULL, 2, NULL),
	(19, 'LENGUAJE VISUAL II', '5', '13', NULL, NULL, 2, NULL),
	(20, 'TEORÍA DE LA PERCEPCIÓN Y LA COMUNICACIÓN', '2', NULL, NULL, NULL, 2, NULL),
	(21, 'HISTORIA DEL ARTE II/HISTORIA DE LAS ARTES VISUALES II', '5', '14', NULL, NULL, 2, NULL),
	(22, 'CERÁMICA Y ALFARERÍA(DECORACIÓN/ALFARERÍA/MODELADO) ', '2', NULL, NULL, NULL, 2, NULL),
	(23, 'PROYECTO Y DISEÑO CERÁMICO II/DIBUJO III', '5', '16,19', NULL, NULL, 3, NULL),
	(24, 'TECNOLOGÍA APLICADA A LA CERÁMICA II', '2', NULL, NULL, NULL, 3, NULL),
	(25, 'ARTES, CULTURAS Y ESTÉTICAS EN EL MUNDO CONTEMPORÁNEO (MODELADO)', '2', NULL, NULL, NULL, 3, NULL),
	(26, 'HISTORIA DE LA CERÁMICA Y PROYECTO DE ANÁLISIS', '2', NULL, NULL, NULL, 3, NULL),
	(27, 'ESPACIO INSTITUCIONAL (LENGUAJE VISUAL)', '2', NULL, NULL, NULL, 3, NULL),
	(28, 'CERÁMICA-MOLDERÍA-ALFARERÍA (MODELADO/MATRICERÍA/ALFARERÍA)/CERÁMICA III', '5', '35,17,19,16', NULL, NULL, 3, NULL),
	(29, 'CERÁMICA I (ALFARERÍA/MOLDERÍA/DECORACIÓN)', '3', NULL, NULL, NULL, 1, NULL),
	(30, 'TALLER COMPLEMENTARIO (ESCULTURA/MODELADO)', '3', NULL, NULL, NULL, 1, NULL),
	(31, 'PRÁCTICA DOCENTE I', '3', NULL, NULL, NULL, 1, NULL),
	(32, 'PSICOLOGÍA DE LA EDUCACIÓN I', '3', NULL, NULL, NULL, 1, NULL),
	(33, 'FUNDAMENTOS DE LA EDUCACIÓN', '3', NULL, NULL, NULL, 1, NULL),
	(34, 'HISTORIA SOCIAL GENERAL', '3', NULL, NULL, NULL, 1, NULL),
	(35, 'CERÁMICA II (DECORACIÓN/ALFARERÍA)', '3', '29,10,13,9', NULL, NULL, 2, NULL),
	(36, 'TALLER COMPLEMENTARIO II (ESCULTURA/MODELADO)', '3', '30,9,13', NULL, NULL, 2, NULL),
	(37, 'PRÁCTICA DOCENTE II', '3', '31,33,32', NULL, NULL, 2, NULL),
	(38, 'HISTORIA SOCIOPOLÍTICA DE LATINOAMÉRICA Y ARGENTINA', '3', '34', NULL, NULL, 2, NULL),
	(39, 'DIDÁCTICA GENERAL', '3', '33,32', NULL, NULL, 2, NULL),
	(40, 'PSICOLOGÍA DE LA EDUCACIÓN II', '3', '33,32', NULL, NULL, 2, NULL),
	(41, 'LENGUAJE VISUAL III', '3', '19', NULL, NULL, 3, NULL),
	(42, 'DIDÁCTICA DE LAS ARTES VISUALES I', '3', '39,40,37', NULL, NULL, 3, NULL),
	(43, 'QUÍMICA APLICADA II', '3', '17,35', NULL, NULL, 3, NULL),
	(44, 'MEDIOS AUDIOVISUALES E IMAGEN DIGITAL', '3', '19,16', NULL, NULL, 3, NULL),
	(45, 'HISTORIAS DE LAS ARTES VISUALES III', '3', '21', NULL, NULL, 3, NULL),
	(46, 'PRÁCTICA DOCENTE III', '3', '19,16,35,17,36,21,37,38,39,40', NULL, NULL, 3, 42),
	(47, 'POLÍTICA EDUCATIVA', '3', '39,38', NULL, NULL, 3, NULL),
	(48, 'TEORÍAS DEL ARTE I', '3', '38,21', NULL, NULL, 3, NULL),
	(49, 'CERÁMICA IV', '3', '42,41,23', NULL, NULL, 4, NULL),
	(50, 'DIBUJO IV', '3', '41,23', NULL, NULL, 4, NULL),
	(51, 'ARTES COMBINADAS', '3', '23,16,36', NULL, NULL, 4, NULL),
	(52, 'DIDÁCTICA DE LAS ARTES VISUALES II', '3', '42,47', NULL, NULL, 4, NULL),
	(53, 'PRÁCTICA DOCENTE IV', '3', '41,23,28,43,44,45,42,46,47,48', NULL, NULL, 4, 52),
	(54, 'TEORÍAS DEL ARTE II', '3', '48,45', NULL, NULL, 4, NULL),
	(55, 'METODOLOGÍA DE LA INVESTIGACIÓN', '3', '48,45', NULL, NULL, 4, NULL);
/*!40000 ALTER TABLE `asignaturas` ENABLE KEYS */;


-- Volcando estructura para tabla imca.calificaciones
CREATE TABLE IF NOT EXISTS `calificaciones` (
  `id_calif` int(11) NOT NULL AUTO_INCREMENT,
  `id_asign` int(11) NOT NULL,
  `cuatri1` int(11) NOT NULL,
  `cuatri2` int(11) NOT NULL,
  `recup` int(11) DEFAULT NULL,
  `final1` int(11) NOT NULL,
  `final2` int(11) DEFAULT NULL,
  `final3` int(11) DEFAULT NULL,
  `final4` int(11) DEFAULT NULL,
  `nota` int(11) DEFAULT NULL,
  `fecha_final` date NOT NULL,
  PRIMARY KEY (`id_calif`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla imca.calificaciones: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `calificaciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `calificaciones` ENABLE KEYS */;


-- Volcando estructura para tabla imca.carreras
CREATE TABLE IF NOT EXISTS `carreras` (
  `id_carrera` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla imca.carreras: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `carreras` DISABLE KEYS */;
REPLACE INTO `carreras` (`id_carrera`, `nombre`) VALUES
	(1, 'FOBA'),
	(2, 'TECNICATURA'),
	(3, 'LICENCIATURA EN ARTES VISUALES'),
	(4, 'CURSOS EXTRAPROGRAMATICOS'),
	(5, 'AMBAS');
/*!40000 ALTER TABLE `carreras` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
