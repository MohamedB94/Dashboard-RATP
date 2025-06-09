-- Création de la table ratp
CREATE TABLE IF NOT EXISTS ratp (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertion des données de test
INSERT INTO ratp (name, description) VALUES
('1', 'Trafic normal'),
('2', 'Trafic normal'),
('3', 'Trafic normal'),
('3bis', 'Trafic normal'),
('4', 'Trafic normal'),
('5', 'Trafic normal'),
('6', 'Trafic normal'),
('7', 'Trafic normal'),
('7bis', 'Trafic normal'),
('8', 'Trafic normal'),
('9', 'Trafic normal'),
('10', 'Trafic normal'),
('11', 'Trafic normal'),
('12', 'Trafic normal'),
('13', 'Trafic normal'),
('14', 'Trafic normal'); 