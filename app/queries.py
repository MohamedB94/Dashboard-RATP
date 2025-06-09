import pandas as pd
import logging
from datetime import datetime
from app.db import get_connection

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_fiabilite():
    """Récupère les données de fiabilité des lignes"""
    try:
        conn = get_connection()
        query = """
            SELECT 
                name as ligne,
                COUNT(*) as total,
                SUM(CASE WHEN LOWER(description) LIKE '%normal%' THEN 1 ELSE 0 END) as normaux,
                ROUND(SUM(CASE WHEN LOWER(description) LIKE '%normal%' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as fiabilite
            FROM ratp
            WHERE name IS NOT NULL AND name != ''
            GROUP BY name
            ORDER BY CAST(name AS DECIMAL(10,2))
        """
        df = pd.read_sql(query, conn)
        logger.info(f"Données de fiabilité récupérées: {len(df)} lignes")
        return df
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des données de fiabilité: {e}")
        return pd.DataFrame()
    finally:
        if 'conn' in locals():
            conn.close()

def get_current_status():
    """Récupère l'état actuel des lignes"""
    try:
        conn = get_connection()
        query = """
            SELECT 
                name,
                description,
                created_at
            FROM ratp
            WHERE name IS NOT NULL AND name != ''
            ORDER BY CAST(name AS DECIMAL(10,2))
        """
        df = pd.read_sql(query, conn)
        if not df.empty:
            df['created_at'] = pd.to_datetime(df['created_at'])
        logger.info(f"Données d'état récupérées: {len(df)} lignes")
        return df
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des données d'état: {e}")
        return pd.DataFrame()
    finally:
        if 'conn' in locals():
            conn.close() 