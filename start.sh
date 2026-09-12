#!/bin/bash

# ============================================
# Jarvis Discord Bot - Quick Start
# ============================================

show_menu() {
    clear
    echo ""
    echo "╔════════════════════════════════════════════╗"
    echo "║     🤖 JARVIS - Démarrage Rapide 🤖       ║"
    echo "╚════════════════════════════════════════════╝"
    echo ""
    echo "1. Démarrer le bot"
    echo "2. Ouvrir le launcher complet"
    echo "3. Configurer le bot"
    echo "4. Installer les dépendances"
    echo "5. Quitter"
    echo ""
    read -p "Choisissez une option (1-5): " choice
}

start_bot() {
    clear
    echo ""
    echo "🚀 Démarrage du bot Jarvis..."
    echo ""
    
    if [ ! -f ".env" ]; then
        echo "❌ Fichier .env manquant!"
        echo ""
        read -p "Voulez-vous configurer le bot? (y/n): " configure
        if [ "$configure" = "y" ] || [ "$configure" = "Y" ]; then
            config_bot
        fi
        read -p "[Appuyez sur Entrée pour continuer...]"
        show_menu
        return
    fi
    
    if [ ! -f "main.py" ]; then
        echo "❌ Le fichier main.py n'existe pas!"
        read -p "[Appuyez sur Entrée pour continuer...]"
        show_menu
        return
    fi
    
    if [ -f "venv/bin/python" ]; then
        echo "✅ Utilisation de l'environnement virtuel"
        venv/bin/python main.py
    else
        echo "⚠️  Environnement virtuel non trouvé, utilisation de Python par défaut"
        python main.py
    fi
    
    echo ""
    echo "⏹️  Bot arrêté"
    read -p "[Appuyez sur Entrée pour continuer...]"
    show_menu
}

launcher() {
    clear
    echo ""
    echo "📋 Lancement du launcher interactif..."
    echo ""
    python launcher.py
    show_menu
}

config_bot() {
    clear
    echo ""
    echo "⚙️  Configuration du bot..."
    echo ""
    
    if [ ! -f "setup.py" ]; then
        echo "❌ Le fichier setup.py n'existe pas!"
        read -p "[Appuyez sur Entrée pour continuer...]"
        show_menu
        return
    fi
    
    python setup.py
    read -p "[Appuyez sur Entrée pour continuer...]"
    show_menu
}

install_deps() {
    clear
    echo ""
    echo "📦 Installation des dépendances..."
    echo ""
    
    if [ ! -d "venv" ]; then
        echo "🔧 Création de l'environnement virtuel..."
        python -m venv venv
        echo "✅ Environnement virtuel créé"
        echo ""
    fi
    
    echo "📥 Installation des packages..."
    if [ -f "venv/bin/pip" ]; then
        venv/bin/pip install -r requirements.txt
    else
        pip install -r requirements.txt
    fi
    
    echo ""
    echo "✅ Dépendances installées!"
    read -p "[Appuyez sur Entrée pour continuer...]"
    show_menu
}

while true; do
    show_menu
    
    case $choice in
        1)
            start_bot
            ;;
        2)
            launcher
            ;;
        3)
            config_bot
            ;;
        4)
            install_deps
            ;;
        5)
            clear
            echo ""
            echo "👋 Au revoir!"
            echo ""
            exit 0
            ;;
        *)
            echo ""
            echo "❌ Option invalide!"
            read -p "[Appuyez sur Entrée pour continuer...]"
            ;;
    esac
done
