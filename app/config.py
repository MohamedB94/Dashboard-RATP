import pymysql
import os
import logging
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration de la base de données
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'mysql'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'ratp_user'),
    'password': os.getenv('DB_PASSWORD', 'ratp_password'),
    'database': os.getenv('DB_NAME', 'ratp_db')
}

# Configuration de l'API
API_CONFIG = {
    'api_key': os.getenv('API_KEY', ''),
    'base_url': os.getenv('API_BASE_URL', '')
}

def get_connection():
    """Crée une connexion à la base de données en utilisant la configuration DB_CONFIG"""
    try:
        connection = pymysql.connect(**DB_CONFIG)
        logger.info("Connexion à la base de données réussie!")
        return connection
    except pymysql.MySQLError as e:
        logger.error(f"Erreur de connexion à la base de données : {e}")
        raise

# Vérification de la configuration
def check_config():
    """Vérifie que toutes les configurations nécessaires sont présentes"""
    logger.info("Vérification de la configuration...")
    logger.info(f"Configuration de la base de données: {DB_CONFIG}")
    logger.info(f"URL de l'API: {API_CONFIG['base_url']}")
    logger.info(f"Clé API présente: {'Oui' if API_CONFIG['api_key'] else 'Non'}")

if __name__ == "__main__":
    check_config() 