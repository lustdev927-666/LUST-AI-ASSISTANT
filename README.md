# LUST AI Assistant

🤖 Un assistant IA moderne, elegant et intelligent pour Telegram avec support multi-personnalites

**Cree par:** @LustDeveloper  
**Version:** 1.0.0  
**Statut:** Actif ✅

---

## 📋 Table des matieres

- [Presentation](#presentation)
- [Fonctionnalites](#fonctionnalites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Commandes](#commandes)
- [Technologies](#technologies)
- [Credits](#credits)

## 🤖 Presentation

LUST AI Assistant est un bot Telegram puissant et versatile qui offre:
- 7 personnalites IA uniques et engageantes
- Conversations avec memoire intelligente
- Support du francais et de l'anglais
- Interface utilisateur intuitive et elegante
- Gestion securisee des donnees

## ✨ Fonctionnalites

- **Multi-Personnalites:** 7 styles de conversation differents
  - Lust (Equilibre)
  - Dark Mind (Mysterieux)
  - Anime Senpai (Fan d'anime)
  - Hacker Mentor (Expert technique)
  - Philosopher (Penseur)
  - Python Developer (Expert Python)
  - Professional Assistant (Aide professionnelle)

- **Memoire de Conversation:** Le bot se souvient du contexte
- **Support Bilingue:** Francais et Anglais
- **Base de Donnees SQLite:** Stockage securise des conversations
- **Formattage Markdown:** Reponses bien presentees
- **Commandes Intuitives:** Interface facile a utiliser

## 📦 Installation

### Prerequis

- Python 3.11 ou superieur
- pip (gestionnaire de paquets Python)
- Un token Telegram Bot (obtenu via @BotFather)
- Une cle API OpenAI

### Installation sur Linux

```bash
# Mettre a jour les paquets
pkg update -y
pkg upgrade -y

# Installer Python et Git
pkg install python git -y

# Cloner le repository
git clone https://github.com/lustdev927-666/LUST-AI-ASSISTANT.git

# Naviguer dans le dossier
cd LUST-AI-ASSISTANT

# Installer les dependances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
nano .env
```

### Installation sur Windows

```bash
# Cloner le repository
git clone https://github.com/lustdev927-666/LUST-AI-ASSISTANT.git

# Naviguer dans le dossier
cd LUST-AI-ASSISTANT

# Installer les dependances
pip install -r requirements.txt

# Configurer les variables d'environnement
copy .env.example .env
# Editer .env avec votre editeur prefere
```

### Installation sur VPS

```bash
# Connexion SSH a votre VPS
ssh user@your_vps_ip

# Mettre a jour le systeme
sudo apt update
sudo apt upgrade -y

# Installer les paquets necessaires
sudo apt install python3 python3-pip git -y

# Cloner le repository
git clone https://github.com/lustdev927-666/LUST-AI-ASSISTANT.git
cd LUST-AI-ASSISTANT

# Installer les dependances Python
pip3 install -r requirements.txt

# Configurer le fichier .env
cp .env.example .env
nano .env
```

### Installation avec Termux (Android)

```bash
# Mettre a jour Termux
pkg update -y
pkg upgrade -y

# Installer les outils necessaires
pkg install python git -y

# Cloner le repository
git clone https://github.com/lustdev927-666/LUST-AI-ASSISTANT.git
cd LUST-AI-ASSISTANT

# Installer les dependances
pip install -r requirements.txt

# Configurer les variables
cp .env.example .env
nano .env
```

## ⚙️ Configuration

### Variables d'environnement (.env)

Creez un fichier `.env` a la racine du projet:

```
TELEGRAM_BOT_TOKEN=votre_token_telegram
OPENAI_API_KEY=votre_cle_openai
DATABASE_PATH=data/users.db
LOG_LEVEL=INFO
```

### Obtenir les tokens

**Token Telegram:**
1. Ouvrez Telegram
2. Cherchez @BotFather
3. Envoyez `/newbot`
4. Suivez les instructions
5. Copiez votre token

**Cle OpenAI:**
1. Allez sur https://platform.openai.com/api-keys
2. Creez une nouvelle cle API
3. Copiez-la dans votre `.env`

## 🚀 Utilisation

### Demarrer le bot

```bash
python bot.py
```

Le bot est maintenant actif et pret a traiter les messages!

### Deploiement sur Railway

1. Poussez votre code sur GitHub
2. Connectez-vous a https://railway.app
3. Creez un nouveau projet
4. Selectionnez GitHub et choisissez votre repo
5. Ajoutez les variables d'environnement
6. Deployez!

### Deploiement sur Render

1. Poussez votre code sur GitHub
2. Allez sur https://render.com
3. Creez un nouveau service Web
4. Selectionnez votre repository
5. Configurez les variables d'environnement
6. Deployez!

## 💬 Commandes

| Commande | Description |
|----------|-------------|
| `/start` | Initialiser le bot et choisir une personnalite |
| `/help` | Afficher le guide complet d'utilisation |
| `/about` | Informations sur le bot |
| `/ai <question>` | Poser une question a l'IA |
| `/personality` | Changer de personnalite |
| `/history` | Voir les 10 dernieres conversations |
| `/stats` | Afficher les statistiques du bot |
| `/reset` | Effacer votre historique |
| `/ping` | Verifier que le bot fonctionne |

## 🛠️ Technologies

- **Python 3.11+** - Langage de programmation
- **python-telegram-bot** - Wrapper Telegram
- **OpenAI API** - Intelligence artificielle
- **SQLite** - Base de donnees
- **python-dotenv** - Gestion des variables d'environnement

## 📊 Structure du projet

```
LUST-AI-ASSISTANT/
├── bot.py                 # Fichier principal
├── config.py              # Configuration
├── database.py            # Gestion base de donnees
├── ai.py                  # Integration OpenAI
├── handlers/
│   ├── __init__.py
│   ├── start.py           # Commandes de demarrage
│   ├── ai_handler.py      # Gestion IA
│   └── admin.py           # Commandes admin
├── data/
│   └── users.db           # Base de donnees
├── logs/                  # Fichiers journaux
├── .env.example           # Template .env
├── requirements.txt       # Dependances Python
└── README.md              # Ce fichier
```

## 👨‍💻 Credits

**Developpe par:** @LustDeveloper  
**Avec ❤️** pour la communaute

- GitHub: https://github.com/lustdev927-666
- Repository: https://github.com/lustdev927-666/LUST-AI-ASSISTANT

## 📝 Licence

Ce projet est open source et disponible sous licence MIT.

## 🤝 Contribution

Les contributions sont bienvenues! Pour contribuer:

1. Forkez le projet
2. Creez une branche pour votre feature
3. Commitez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## 📞 Support

Si vous avez des questions ou rencontrez des problemes:
1. Consultez la documentation
2. Verifiez que vos variables .env sont correctes
3. Assurez-vous que vos cles API sont valides
4. Ouvrez une issue sur GitHub

---

**Version:** 1.0.0  
**Statut:** Actif ✅  
**Cree par:** @LustDeveloper  
**Derniere mise a jour:** 2026-06-09
