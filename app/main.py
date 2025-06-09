import streamlit as st
import pandas as pd
from datetime import datetime
import logging
import json
import sys
import os

# Ajout du répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db import create_Table
from app.fetch_api import fetch_and_store
from app.queries import get_fiabilite, get_current_status

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration de la page
st.set_page_config(
    page_title="Métro RATP - État des Lignes",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialisation de la base de données
try:
    create_Table()
    logger.info("Base de données initialisée avec succès")
except Exception as e:
    logger.error(f"Erreur lors de l'initialisation de la base de données: {e}")
    st.error("Erreur lors de l'initialisation de la base de données")

# Fonction pour rafraîchir les données
def refresh_data():
    try:
        fetch_and_store()
        logger.info("Données rafraîchies avec succès")
        st.success("Données mises à jour avec succès")
    except Exception as e:
        logger.error(f"Erreur lors du rafraîchissement des données: {e}")
        st.error("Erreur lors de la mise à jour des données")

# Interface utilisateur
st.title("🚇 Métro RATP - État des Lignes")

# Bouton de rafraîchissement
if st.button("🔄 Rafraîchir les données"):
    refresh_data()

# Récupération des données
try:
    status_df = get_current_status()
    fiabilite_df = get_fiabilite()
    
    logger.info(f"Status DataFrame: {status_df.to_dict() if not status_df.empty else 'Empty'}")
    logger.info(f"Fiabilité DataFrame: {fiabilite_df.to_dict() if not fiabilite_df.empty else 'Empty'}")
    
    if status_df.empty or fiabilite_df.empty:
        logger.warning("Données vides détectées, tentative de rafraîchissement")
        refresh_data()
        status_df = get_current_status()
        fiabilite_df = get_fiabilite()
except Exception as e:
    logger.error(f"Erreur lors de la récupération des données: {e}")
    st.error("Erreur lors de la récupération des données")
    refresh_data()
    status_df = get_current_status()
    fiabilite_df = get_fiabilite()

# Affichage de l'état des lignes
st.header("État des lignes")
if not status_df.empty:
    # Trier les lignes par numéro
    status_df['ligne_num'] = pd.to_numeric(status_df['name'], errors='coerce')
    status_df = status_df.sort_values('ligne_num')
    
    for _, ligne in status_df.iterrows():
        with st.expander(f"Ligne {ligne['name']}", expanded=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                if "normal" in str(ligne['description']).lower():
                    st.success(f"✅ Trafic normal")
                else:
                    st.error(f"⚠️ Perturbation")
                st.write(str(ligne['description']))
            with col2:
                try:
                    created_at = ligne['created_at']
                    if isinstance(created_at, pd.Timestamp):
                        st.info(f"Dernière mise à jour:\n{created_at.strftime('%d/%m/%Y %H:%M:%S')}")
                    else:
                        st.info(f"Dernière mise à jour:\n{created_at}")
                except Exception as e:
                    logger.error(f"Erreur lors du formatage de la date: {e}")
                    st.info("Dernière mise à jour: Non disponible")
else:
    st.warning("Aucune donnée d'état disponible")

# Affichage de la fiabilité
st.header("Fiabilité des lignes")
if not fiabilite_df.empty:
    try:
        # Formatage des données
        fiabilite_df['fiabilite'] = pd.to_numeric(fiabilite_df['fiabilite'], errors='coerce')
        fiabilite_df['total'] = pd.to_numeric(fiabilite_df['total'], errors='coerce')
        fiabilite_df['normaux'] = pd.to_numeric(fiabilite_df['normaux'], errors='coerce')
        
        # Trier les lignes par numéro
        fiabilite_df['ligne_num'] = pd.to_numeric(fiabilite_df['ligne'], errors='coerce')
        fiabilite_df = fiabilite_df.sort_values('ligne_num')
        
        # Affichage du tableau
        st.dataframe(
            fiabilite_df[['ligne', 'total', 'normaux', 'fiabilite']],
            use_container_width=True,
            column_config={
                "ligne": "Ligne",
                "total": st.column_config.NumberColumn("Total passages", format="%d"),
                "normaux": st.column_config.NumberColumn("Passages normaux", format="%d"),
                "fiabilite": st.column_config.NumberColumn("Fiabilité (%)", format="%.2f")
            }
        )
        
        # Graphique simple avec Streamlit
        st.subheader("Graphique de fiabilité")
        st.bar_chart(
            fiabilite_df.set_index("ligne")["fiabilite"],
            use_container_width=True
        )
        
    except Exception as e:
        logger.error(f"Erreur lors de l'affichage des données de fiabilité: {e}")
        st.error("Erreur lors de l'affichage des données de fiabilité")
else:
    st.warning("Aucune donnée de fiabilité disponible")

# Pied de page
st.markdown("---")
st.markdown(f"*Dernière mise à jour: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*") 