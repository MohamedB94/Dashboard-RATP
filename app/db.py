import mysql.connector
import logging
from app.config import DB_CONFIG

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        logger.info("Connexion à la base de données établie avec succès")
        return connection
    except mysql.connector.Error as err:
        logger.error(f"Erreur de connexion à la base de données: {err}")
        raise

def create_Table():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Vérification de l'existence de la table
        cursor.execute("SHOW TABLES LIKE 'ratp'")
        if not cursor.fetchone():
            logger.info("Création de la table ratp...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ratp (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            logger.info("Table ratp créée avec succès")
        
        # Vérification du contenu de la table
        cursor.execute("SELECT COUNT(*) FROM ratp")
        count = cursor.fetchone()[0]
        logger.info(f"Nombre de lignes dans la table ratp: {count}")
        
        if count == 0:
            logger.info("Insertion des données de test...")
            test_data = [
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
                ('14', 'Trafic normal')
            ]
            cursor.executemany(
                "INSERT INTO ratp (name, description) VALUES (%s, %s)",
                test_data
            )
            conn.commit()
            logger.info(f"{len(test_data)} lignes insérées avec succès")
        
        # Vérification finale
        cursor.execute("SELECT * FROM ratp")
        rows = cursor.fetchall()
        logger.info(f"Contenu de la table ratp: {rows}")
        
    except mysql.connector.Error as err:
        logger.error(f"Erreur lors de la création/initialisation de la table: {err}")
        raise
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
            logger.info("Connexion à la base de données fermée")

def check_database_content():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            # Vérifier la structure
            cursor.execute("DESCRIBE ratp")
            columns = cursor.fetchall()
            logger.info(f"Structure de la table: {columns}")

            # Vérifier le contenu
            cursor.execute("SELECT * FROM ratp")
            rows = cursor.fetchall()
            logger.info(f"Contenu de la table: {rows}")

            # Vérifier les types de données
            cursor.execute("SELECT name, description, created_at FROM ratp LIMIT 1")
            sample = cursor.fetchone()
            if sample:
                logger.info(f"Types de données - name: {type(sample[0])}, description: {type(sample[1])}, created_at: {type(sample[2])}")

    except Exception as e:
        logger.error(f"Erreur lors de la vérification du contenu: {e}")
        raise
    finally:
        connection.close()

# Appeler la vérification au démarrage
if __name__ == "__main__":
    create_Table()
    check_database_content() 