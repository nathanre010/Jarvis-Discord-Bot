# 🤖 Guide de Configuration - Jarvis Discord Bot

## 📋 Prérequis

- Python 3.8 ou supérieur
- Un compte Discord
- Un serveur Discord pour tester

## 🚀 Installation Rapide

### 1️⃣ Créer une Application Discord

1. Rendez-vous sur [Discord Developer Portal](https://discord.com/developers/applications)
2. Cliquez sur "New Application"
3. Donnez un nom à votre application (ex: "Jarvis")
4. Acceptez les conditions et créez l'application

### 2️⃣ Créer un Bot

1. Dans les paramètres de votre application, allez sur l'onglet "Bot"
2. Cliquez sur "Add Bot"
3. Sous "TOKEN", cliquez sur "Copy" pour copier votre token
4. ⚠️ **Ne partagez JAMAIS votre token!**

### 3️⃣ Configurer les Permissions

1. Allez dans l'onglet "OAuth2" → "URL Generator"
2. Cochez les scopes:
   - `bot`
   - `applications.commands`
3. Cochez les permissions:
   - Administrator (ou sélectionnez les permissions individuelles)
4. Copiez l'URL générée et ouvrez-la pour inviter le bot sur votre serveur

### 4️⃣ Cloner le Repository

```bash
git clone https://github.com/nathanre010/Jarvis-Discord-Bot.git
cd Jarvis-Discord-Bot
```

### 5️⃣ Installer les Dépendances

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```

### 6️⃣ Configuration

#### Option A: Configuration Automatique

```bash
python setup.py
```

#### Option B: Configuration Manuelle

1. Copiez `.env.example` en `.env`
2. Complétez avec vos informations

### 7️⃣ Lancer le Bot

```bash
python main.py
```

## 🔗 Inviter le Bot

```
https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=8&scope=bot%20applications.commands
```

## ✅ Tester le Bot

```
/help
/ping
/status
```

---

**Bon coding! 🚀**
