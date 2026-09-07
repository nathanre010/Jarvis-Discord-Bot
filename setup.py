#!/usr/bin/env python3
"""
Script de configuration pour Jarvis Discord Bot
Ce script vous aide à configurer le bot avec votre token Discord
"""

import os
from pathlib import Path

def create_env_file():
    """Create .env file with user input"""
    
    print("\n" + "="*60)
    print("🤖 Configuration de Jarvis Discord Bot")
    print("="*60 + "\n")
    
    print("Pour obtenir votre token Discord:")
    print("1. Allez sur: https://discord.com/developers/applications")
    print("2. Créez une nouvelle application (ou sélectionnez-la)")
    print("3. Allez dans 'Bot' → 'Reset Token' pour obtenir le token")
    print("4. Copiez le token (il commence par 'Mzk'...)\n")
    
    # Get Discord Token
    while True:
        token = input("📝 Entrez votre Discord Bot Token: ").strip()
        if not token:
            print("❌ Le token ne peut pas être vide!")
            continue
        break
    
    # Get Bot Owner ID
    print("\n📝 Pour obtenir votre Discord ID:")
    print("1. Activez le mode développeur dans Discord (Utilisateur → Paramètres → Avancé)")
    print("2. Clic droit sur votre nom d'utilisateur → Copier l'ID utilisateur\n")
    
    while True:
        try:
            owner_id = input("Entrez votre Discord ID: ").strip()
            int(owner_id)
            break
        except ValueError:
            print("❌ L'ID doit être un nombre!")
    
    # Get Log Channel ID (optional)
    log_channel_id = input("\n📝 Entrez l'ID du salon des logs (optionnel, appuyez sur Entrée): ").strip()
    if not log_channel_id:
        log_channel_id = "0"
    
    # Create .env file
    env_content = f"""# Discord Bot Configuration
DISCORD_TOKEN={token}
BOT_PREFIX=!
BOT_OWNER_ID={owner_id}

# Server Configuration
LOG_CHANNEL_ID={log_channel_id}
SUPPORT_SERVER=https://discord.gg/yourserver

# Database
DATABASE_URL=sqlite:///./data/database.db

# Features
ENABLE_MUSIC=false
ENABLE_TICKETS=true
ENABLE_LOGS=true
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("\n" + "="*60)
    print("✅ Fichier .env créé avec succès!")
    print("="*60)
    print("\nInformations de configuration:")
    print(f"  • Token: {token[:20]}...")
    print(f"  • Owner ID: {owner_id}")
    print(f"  • Log Channel: {log_channel_id or 'Pas configuré'}")
    print("\n📌 Étapes suivantes:")
    print("1. Installez les dépendances: pip install -r requirements.txt")
    print("2. Lancez le bot: python main.py")
    print("\n💡 Pour inviter le bot sur votre serveur:")
    print("   https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&permissions=8&scope=bot%20applications.commands")
    print("   (Remplacez YOUR_BOT_ID par l'ID de votre bot)\n")

def main():
    """Main function"""
    
    # Check if .env already exists
    if Path('.env').exists():
        print("\n⚠️  Le fichier .env existe déjà!")
        print("Voulez-vous le remplacer? (y/n): ", end="")
        if input().lower() != 'y':
            print("❌ Configuration annulée.")
            return
    
    # Create necessary directories
    os.makedirs('data', exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    os.makedirs('cogs', exist_ok=True)
    
    # Create .env file
    create_env_file()

if __name__ == '__main__':
    main()
