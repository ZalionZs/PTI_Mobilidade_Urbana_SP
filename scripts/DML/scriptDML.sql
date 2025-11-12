-- VIAGENS PROGRAMADAS
INSERT INTO viagens_programadas (trip_id, arrival_time) VALUES
('T001', '06:00:00'),
('T002', '06:10:00'),
('T003', '06:55:00'),
('T004', '17:40:00'),
('T005', '18:05:00');

-- VIAGENS REAIS
INSERT INTO viagens_real (
    trip_id, stop_id, horario_real, lotacao, indice_lotacao,
    real_segundos, previsto_segundos, atraso_segundos, atraso_minutos
) VALUES
('T001', 'S101', '06:03:20', 30, 'Baixa', 21800, 21600, 200, 3.33),
('T002', 'S102', '06:15:10', 10, 'Baixa', 22510, 22200, 310, 5.17),
('T001', 'S103', '06:17:00', 15, 'Baixa', 22620, 21600, 1020, 17.00),
('T003', 'S104', '07:00:00', 55, 'Alta', 25200, 24900, 300, 5.00),
('T004', 'S105', '17:15:10', 70, 'Alta', 62110, 63600, -1490, -24.83),
('T005', 'S106', '18:00:15', 30, 'Baixa', 64815, 65100, -285, -4.75);

-- DIM_TEMPO
INSERT INTO dim_tempo (id_tempo, hora, periodo) VALUES
(1, '06:03:20', 'Manhã'),
(2, '06:15:10', 'Manhã'),
(3, '06:17:00', 'Manhã'),
(4, '07:00:00', 'Manhã'),
(5, '17:15:10', 'Tarde'),
(6, '18:00:15', 'Noite');

-- DIM_VIAGEM
INSERT INTO dim_viagem (id_viagem, trip_id, stop_id) VALUES
(1, 'T001', 'S101'),
(2, 'T002', 'S102'),
(3, 'T001', 'S103'),
(4, 'T003', 'S104'),
(5, 'T004', 'S105'),
(6, 'T005', 'S106');

-- FATO_PONTUALIDADE
INSERT INTO fato_pontualidade (
    id_fato, id_viagem, id_tempo, horario_real, arrival_time,
    atraso_segundos, atraso_minutos, lotacao, indice_lotacao
) VALUES
(1, 1, 1, '06:03:20', '06:00:00', 200, 3.33, 30, 'Baixa'),
(2, 2, 2, '06:15:10', '06:10:00', 310, 5.17, 10, 'Baixa'),
(3, 3, 3, '06:17:00', '06:00:00', 1020, 17.00, 15, 'Baixa'),
(4, 4, 4, '07:00:00', '06:55:00', 300, 5.00, 55, 'Alta'),
(5, 5, 5, '17:15:10', '17:40:00', -1490, -24.83, 70, 'Alta'),
(6, 6, 6, '18:00:15', '18:05:00', -285, -4.75, 30, 'Baixa');
