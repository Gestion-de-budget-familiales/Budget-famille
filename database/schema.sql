-- ============================================
-- Projet NIFOO - Budget Familiale
-- Chef: Nirina
-- Base de données: budget_familiale
-- ============================================

CREATE DATABASE IF NOT EXISTS budget_familiale 
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE budget_familiale;

-- Familles
CREATE TABLE IF NOT EXISTS familles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    code_invitation VARCHAR(20) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Utilisateurs (bcrypt pour mot de passe)
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    famille_id INT NOT NULL,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    role ENUM('chef', 'membre') DEFAULT 'membre',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (famille_id) REFERENCES familles(id) ON DELETE CASCADE
);

-- Catégories
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    type ENUM('revenu', 'depense') NOT NULL,
    icone VARCHAR(50) DEFAULT NULL,
    famille_id INT DEFAULT NULL,
    FOREIGN KEY (famille_id) REFERENCES familles(id) ON DELETE SET NULL
);

-- Revenus
CREATE TABLE IF NOT EXISTS revenus (
    id INT AUTO_INCREMENT PRIMARY KEY,
    famille_id INT NOT NULL,
    utilisateur_id INT NOT NULL,
    categorie_id INT NOT NULL,
    montant DECIMAL(12,2) NOT NULL,
    date_revenu DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (famille_id) REFERENCES familles(id) ON DELETE CASCADE,
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id) ON DELETE CASCADE,
    FOREIGN KEY (categorie_id) REFERENCES categories(id)
);

-- Dépenses
CREATE TABLE IF NOT EXISTS depenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    famille_id INT NOT NULL,
    utilisateur_id INT NOT NULL,
    categorie_id INT NOT NULL,
    montant DECIMAL(12,2) NOT NULL,
    date_depense DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (famille_id) REFERENCES familles(id) ON DELETE CASCADE,
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id) ON DELETE CASCADE,
    FOREIGN KEY (categorie_id) REFERENCES categories(id)
);

-- Budgets mensuels prévisionnels
CREATE TABLE IF NOT EXISTS budgets_mensuels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    famille_id INT NOT NULL,
    categorie_id INT NOT NULL,
    mois INT NOT NULL CHECK (mois BETWEEN 1 AND 12),
    annee INT NOT NULL,
    montant_prevu DECIMAL(12,2) NOT NULL,
    UNIQUE(famille_id, categorie_id, mois, annee),
    FOREIGN KEY (famille_id) REFERENCES familles(id) ON DELETE CASCADE,
    FOREIGN KEY (categorie_id) REFERENCES categories(id)
);

-- Catégories par défaut
INSERT INTO categories (nom, type) VALUES
('Salaire', 'revenu'),
('Vente', 'revenu'),
('Aide familiale', 'revenu'),
('Nourriture', 'depense'),
('Loyer', 'depense'),
('Transport', 'depense'),
('Scolarité', 'depense'),
('Santé', 'depense'),
('Loisirs', 'depense');