-- Viagens programadas
INSERT INTO viagens_programadas (trip_id, arrival_time) VALUES
('T001', '06:00:00'),
('T002', '06:10:00'),
('T003', '06:55:00'),
('T004', '17:40:00'),
('T005', '18:05:00');

-- Viagens reais
INSERT INTO viagens_real (trip_id, stop_id, horario_real, lotacao) VALUES
('T001', 'S101', '06:03:20', 30),
('T002', 'S102', '06:15:10', 10),
('T001', 'S103', '06:17:00', 15),
('T003', 'S104', '07:00:00', 55),
('T004', 'S105', '17:15:10', 70),
('T005', 'S106', '18:00:15', 30);
