# Pipeline RATP - Tableau de Bord de Surveillance

Ce projet est un tableau de bord de surveillance en temps réel pour le réseau RATP, permettant de suivre l'état du trafic sur les différentes lignes de métro.

## 🚀 Fonctionnalités

- Affichage en temps réel de l'état du trafic sur toutes les lignes de métro
- Indicateurs de fiabilité par ligne
- Visualisation des données sous forme de graphiques et tableaux
- Interface utilisateur intuitive et responsive

## 🛠️ Technologies Utilisées

- **Frontend** : Streamlit
- **Backend** : Python
- **Base de données** : MySQL
- **Conteneurisation** : Docker & Docker Compose
- **Visualisation** : Plotly

## 📋 Prérequis

- Docker
- Docker Compose
- Git

## 🚀 Installation

1. Clonez le dépôt :

```bash
git clone [https://github.com/MohamedB94/Dashboard-RATP]
cd Pipeline-RATP
```

2. Configurez les variables d'environnement :

```bash
cp .env.example .env
```

Modifiez le fichier `.env` avec vos paramètres de base de données.

3. Démarrez l'application avec Docker Compose :

```bash
docker-compose up --build
```

4. Accédez à l'application dans votre navigateur :

```
http://localhost:8501
```

## 📁 Structure du Projet

```
Pipeline-RATP/
├── app/
│   ├── main.py          # Point d'entrée de l'application
│   ├── db.py            # Configuration de la base de données
│   ├── queries.py       # Requêtes SQL
│   └── config.py        # Configuration de l'application
├── docker/
│   └── mysql/           # Configuration MySQL
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🔧 Configuration

### Variables d'Environnement

- `MYSQL_ROOT_PASSWORD` : Mot de passe root MySQL
- `MYSQL_DATABASE` : Nom de la base de données
- `MYSQL_USER` : Utilisateur MySQL
- `MYSQL_PASSWORD` : Mot de passe utilisateur MySQL
- `MYSQL_HOST` : Hôte MySQL
- `MYSQL_PORT` : Port MySQL

## 📊 Fonctionnalités Principales

1. **Tableau de Bord Principal**

   - Vue d'ensemble de l'état du trafic
   - Indicateurs de fiabilité par ligne
   - Mise à jour en temps réel

2. **Statistiques**

   - Taux de fiabilité par ligne
   - Historique des perturbations
   - Tendances et analyses

3. **Gestion des Données**
   - Synchronisation automatique avec l'API RATP
   - Stockage optimisé dans MySQL
   - Requêtes optimisées pour les performances

## ⚠️ Disclaimer

Ce projet a été développé dans un temps limité et présente certaines limitations :

- Les données affichées peuvent ne pas être 100% fiables ou à jour
- La synchronisation avec l'API RATP pourrait nécessiter des optimisations
- Certaines fonctionnalités pourraient être améliorées ou optimisées
- La gestion des erreurs et des cas limites pourrait être renforcée

Ces points sont identifiés comme des axes d'amélioration pour les futures versions du projet.

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Auteurs

- Votre Nom - Développeur Principal

## 🙏 Remerciements

- RATP pour l'API de données
