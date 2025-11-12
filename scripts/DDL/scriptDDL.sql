-- Criar o banco
CREATE DATABASE transporte;
USE transporte;


-- Viagens programadas (dados teóricos)
CREATE TABLE viagens_programadas (
    trip_id VARCHAR(10) PRIMARY KEY,
    arrival_time TIME NOT NULL
);

-- Viagens reais (dados observados)
CREATE TABLE viagens_real (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id VARCHAR(10) NOT NULL,
    stop_id VARCHAR(10) NOT NULL,
    horario_real TIME NOT NULL,
    lotacao INT NOT NULL,
    indice_lotacao VARCHAR(10),
    real_segundos INT,
    previsto_segundos INT,
    atraso_segundos INT,
    atraso_minutos FLOAT,
    FOREIGN KEY (trip_id) REFERENCES viagens_programadas(trip_id)
);

-- ==========================================
-- DATA WAREHOUSE
-- ==========================================

-- Dimensão do tempo
CREATE TABLE dim_tempo (
    id_tempo INT AUTO_INCREMENT PRIMARY KEY,
    hora TIME NOT NULL,
    periodo VARCHAR(10)  -- manhã, tarde, noite
);

-- Dimensão da viagem
CREATE TABLE dim_viagem (
    id_viagem INT AUTO_INCREMENT PRIMARY KEY,
    trip_id VARCHAR(10) NOT NULL,
    stop_id VARCHAR(10) NOT NULL
);

-- Fato de pontualidade
CREATE TABLE fato_pontualidade (
    id_fato INT AUTO_INCREMENT PRIMARY KEY,
    id_viagem INT,
    id_tempo INT,
    horario_real TIME,
    arrival_time TIME,
    atraso_segundos INT,
    atraso_minutos FLOAT,
    lotacao INT,
    indice_lotacao VARCHAR(10),
    FOREIGN KEY (id_viagem) REFERENCES dim_viagem(id_viagem),
    FOREIGN KEY (id_tempo) REFERENCES dim_tempo(id_tempo)
);







