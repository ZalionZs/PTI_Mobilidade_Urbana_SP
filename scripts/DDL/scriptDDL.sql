-- Criar o banco
CREATE DATABASE transporte;
USE transporte;

-- Tabela de viagens programadas
CREATE TABLE viagens_programadas (
    trip_id VARCHAR(10) PRIMARY KEY,
    arrival_time TIME NOT NULL
);

-- Tabela de viagens reais
CREATE TABLE viagens_real (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id VARCHAR(10) NOT NULL,
    stop_id VARCHAR(10) NOT NULL,
    horario_real TIME NOT NULL,
    lotacao INT,
    FOREIGN KEY (trip_id) REFERENCES viagens_programadas(trip_id)
);

--Criação do DW

CREATE TABLE dim_tempo (
    id_tempo INT AUTO_INCREMENT PRIMARY KEY,
    hora TIME,
    periodo VARCHAR(10)  -- manhã, tarde, noite etc.
);

CREATE TABLE dim_viagem (
    id_viagem INT AUTO_INCREMENT PRIMARY KEY,
    trip_id VARCHAR(10),
    stop_id VARCHAR(10)
);

CREATE TABLE fato_pontualidade (
    id_fato INT AUTO_INCREMENT PRIMARY KEY,
    id_viagem INT,
    id_tempo INT,
    horario_real TIME,
    arrival_time TIME,
    atraso_segundos INT,
    lotacao INT,
    FOREIGN KEY (id_viagem) REFERENCES dim_viagem(id_viagem),
    FOREIGN KEY (id_tempo) REFERENCES dim_tempo(id_tempo)
);

