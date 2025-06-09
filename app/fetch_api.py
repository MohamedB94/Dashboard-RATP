import requests
import logging
from datetime import datetime
import json
from app.db import get_connection

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def fetch_and_store():
    """Récupère les données de l'API et les stocke dans la base de données"""
    try:
        # Connexion à la base de données
        conn = get_connection()
        if not conn:
            logger.error("Impossible de se connecter à la base de données")
            return False
            
        cursor = conn.cursor()
        
        # Vider la table existante
        cursor.execute("TRUNCATE TABLE ratp")
        logger.info("Table ratp vidée")
        
        # Données de test pour les 14 lignes de métro
        test_data = [
            ("1", "Trafic normal sur la ligne 1"),
            ("2", "Perturbations sur la ligne 2 - Trafic perturbé"),
            ("3", "Trafic normal sur la ligne 3"),
            ("4", "Travaux sur la ligne 4 - Trafic perturbé"),
            ("5", "Trafic normal sur la ligne 5"),
            ("6", "Perturbations sur la ligne 6 - Trafic perturbé"),
            ("7", "Trafic normal sur la ligne 7"),
            ("8", "Travaux sur la ligne 8 - Trafic perturbé"),
            ("9", "Trafic normal sur la ligne 9"),
            ("10", "Perturbations sur la ligne 10 - Trafic perturbé"),
            ("11", "Trafic normal sur la ligne 11"),
            ("12", "Travaux sur la ligne 12 - Trafic perturbé"),
            ("13", "Trafic normal sur la ligne 13"),
            ("14", "Perturbations sur la ligne 14 - Trafic perturbé")
        ]
        
        # Insertion des données de test
        for name, description in test_data:
            try:
                cursor.execute(
                    "INSERT INTO ratp (name, description, created_at) VALUES (%s, %s, NOW())",
                    (name, description)
                )
                logger.info(f"Donnée insérée: {name} - {description}")
            except Exception as e:
                logger.error(f"Erreur lors de l'insertion de la ligne {name}: {e}")
        
        # Vérification des données insérées
        cursor.execute("SELECT COUNT(*) FROM ratp")
        count = cursor.fetchone()[0]
        logger.info(f"Nombre total de lignes insérées: {count}")
        
        # Vérification du contenu
        cursor.execute("SELECT * FROM ratp ORDER BY name")
        rows = cursor.fetchall()
        logger.info(f"Contenu de la table: {rows}")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return True
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération/stockage des données: {e}")
        return False

if __name__ == "__main__":
    fetch_and_store() 